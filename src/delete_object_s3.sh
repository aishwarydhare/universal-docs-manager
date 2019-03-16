#!/bin/sh -u

# To the extent possible under law, Viktor Szakats (vszakats.net)
# has waived all copyright and related or neighboring rights to this
# script.
# CC0 - https://creativecommons.org/publicdomain/zero/1.0/

# Upload a file to Amazon AWS S3 using Signature Version 4
#
# docs:
#    https://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html
#
# requires:
#    curl, openssl 1.x, GNU sed, LF EOLs in this file

objectName="${1:-example-local-file.ext}"
bucket="${2:-example-bucket}"
region="${3:-}"

m_openssl() {
  if [ -f /usr/local/opt/openssl@1.1/bin/openssl ]; then
    /usr/local/opt/openssl@1.1/bin/openssl "$@"
  elif [ -f /usr/local/opt/openssl/bin/openssl ]; then
    /usr/local/opt/openssl/bin/openssl "$@"
  else
    openssl "$@"
  fi
}

m_sed() {
  if which gsed > /dev/null 2>&1; then
    gsed "$@"
  else
    sed "$@"
  fi
}

awsStringSign4() {
  kSecret="AWS4$1"
  kDate=$(printf         '%s' "$2" | m_openssl dgst -sha256 -hex -mac HMAC -macopt "key:${kSecret}"     2>/dev/null | m_sed 's/^.* //')
  kRegion=$(printf       '%s' "$3" | m_openssl dgst -sha256 -hex -mac HMAC -macopt "hexkey:${kDate}"    2>/dev/null | m_sed 's/^.* //')
  kService=$(printf      '%s' "$4" | m_openssl dgst -sha256 -hex -mac HMAC -macopt "hexkey:${kRegion}"  2>/dev/null | m_sed 's/^.* //')
  kSigning=$(printf 'aws4_request' | m_openssl dgst -sha256 -hex -mac HMAC -macopt "hexkey:${kService}" 2>/dev/null | m_sed 's/^.* //')
  signedString=$(printf  '%s' "$5" | m_openssl dgst -sha256 -hex -mac HMAC -macopt "hexkey:${kSigning}" 2>/dev/null | m_sed 's/^.* //')
  printf '%s' "${signedString}"
}

iniGet() {
  # based on: https://stackoverflow.com/questions/22550265/read-certain-key-from-certain-section-of-ini-file-sed-awk#comment34321563_22550640
  printf '%s' "$(m_sed -n -E "/\[$2\]/,/\[.*\]/{/$3/s/(.*)=[ \\t]*(.*)/\2/p}" "$1")"
}

# Initialize access keys

if [ -z "${AWS_CONFIG_FILE:-}" ]; then
  if [ -z "${AWS_ACCESS_KEY:-}" ]; then
    echo 'AWS_CONFIG_FILE or AWS_ACCESS_KEY/AWS_SECRET_KEY envvars not set.'
    exit 1
  else
    awsAccess="${AWS_ACCESS_KEY}"
    awsSecret="${AWS_SECRET_KEY}"
    awsRegion='us-east-1'
  fi
else
  awsProfile='default'

  # Read standard aws-cli configuration file
  # pointed to by the envvar AWS_CONFIG_FILE
  awsAccess="$(iniGet "${AWS_CONFIG_FILE}" "${awsProfile}" 'aws_access_key_id')"
  awsSecret="$(iniGet "${AWS_CONFIG_FILE}" "${awsProfile}" 'aws_secret_access_key')"
  awsRegion="$(iniGet "${AWS_CONFIG_FILE}" "${awsProfile}" 'region')"
fi

# Initialize defaults

if [ -z "${region}" ]; then
  region="${awsRegion}"
fi

echo "Deleting" "${objectName}" "->" "${bucket}" "${region}"
#echo "| $(uname) | $(m_openssl version) | $(m_sed --version | head -1) |"

# Initialize helper variables

httpReq='DELETE'
authType='AWS4-HMAC-SHA256'
service='s3'
baseUrl=".${service}.amazonaws.com"
dateValueS=$(date -u +'%Y%m%d')
dateValueL=$(date -u +'%Y%m%dT%H%M%SZ')

# 0. Create SHA256 hash of an empty string

payloadHash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

# 1. Create canonical request

# NOTE: order significant in ${headerList} and ${canonicalRequest}

headerList='host;x-amz-content-sha256;x-amz-date'

canonicalRequest="\
${httpReq}
/${objectName}

host:${bucket}${baseUrl}
x-amz-content-sha256:${payloadHash}
x-amz-date:${dateValueL}

${headerList}
${payloadHash}"

# Hash it

canonicalRequestHash=$(printf '%s' "${canonicalRequest}" | m_openssl dgst -sha256 -hex 2>/dev/null | m_sed 's/^.* //')

# 2. Create string to sign

stringToSign="\
${authType}
${dateValueL}
${dateValueS}/${region}/${service}/aws4_request
${canonicalRequestHash}"

# 3. Sign the string

signature=$(awsStringSign4 "${awsSecret}" "${dateValueS}" "${region}" "${service}" "${stringToSign}")

# Download

curl -f -s -L --proto-redir =https -X "${httpReq}"\
  -H "Host: ${bucket}${baseUrl}" \
  -H "X-Amz-Content-SHA256: ${payloadHash}" \
  -H "X-Amz-Date: ${dateValueL}" \
  -H "Date: ${dateValueL}" \
  -H "Authorization: ${authType} Credential=${awsAccess}/${dateValueS}/${region}/${service}/aws4_request, SignedHeaders=${headerList}, Signature=${signature}" \
  "https://${bucket}${baseUrl}/${objectName}" || exit 1

exit 0
