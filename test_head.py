import os


class S3ObjectMeta:
    modified_at = None
    name = None
    size = None
    content_type = None
    key = None

    def __init__(self, modified_at, name, size, content_type, path=None):
        self.modified_at = modified_at
        self.name = name
        self.size = size
        self.content_type = content_type
        self.key = path

    def __str__(self):
        return "fileName:\t%s\nmodified_at:\t%s\nsize:\t%s\nsize:\t%s bytes" % (self.name, self.modified_at, self.content_type, self.size)


def parse_response_headers_in_dict(lines):
    d = dict()
    for line in lines:
        sep = line.find(':')
        if sep >= 0:
            key = (line[:sep]).strip()
            val = (line[sep + 1:]).strip()
            d[key] = val
    return d


def get_object_metadata_from_s3(aws_config_file_path: str, object_to_download: str, bucket_name: str, region: str,
                                output_file: str) -> S3ObjectMeta:
    r = os.system("export AWS_CONFIG_FILE='%s' && ./head_object_s3.sh %s %s %s %s"
                  % (aws_config_file_path, object_to_download, bucket_name, region, output_file))
    if not isinstance(r, int):
        print('err', r)
        return None
    elif r != 0:
        print("error")
        return None

    obj_meta = None
    with open(output_file, 'r+') as file:
        d = parse_response_headers_in_dict(file.readlines())
        obj_meta = S3ObjectMeta(d['Last-Modified'], object_to_download.split("/")[-1], d['Content-Length'], d['Content-Type'], object_to_download)
        file.close()
    os.remove(output_file)
    return obj_meta


ret = get_object_metadata_from_s3(
    aws_config_file_path="./.my-aws-config",
    object_to_download='myDirectoryName/myFileName.xml',
    bucket_name='repos-master-bucket',
    region='us-east-2',
    output_file='my_output_file.txt'
)

if ret:
    print("get object metadata successful\n%s" % ret)
else:
    print("request failed")
