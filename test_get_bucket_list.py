import os
import xmltodict
from test_head import S3ObjectMeta


class S3BucketList:
    contents: [S3ObjectMeta]
    bucket_name: str
    bucket_size: int
    directory: str
    raw: dict

    def __init__(self, raw: dict):
        self.raw = raw
        self.name = raw['ListBucketResult']['Name']
        self.bucket_size = raw['ListBucketResult']['KeyCount']
        self.directory = raw['ListBucketResult']['prefix'] if 'prefix' in raw['ListBucketResult'] else ""
        self.contents = []
        for item in raw['ListBucketResult']['Contents']:
            s3_obj = S3ObjectMeta(modified_at=item['LastModified'], name=str(item['Key']).split('/')[-1], size=item['Size'], content_type=None, path=item['Key'])
            self.contents.append(s3_obj)


def get_bucket_list(aws_config_file_path: str, bucket_name: str, region: str,
                    output_file: str, prefix: str="") -> S3BucketList:
    r = os.system("export AWS_CONFIG_FILE='%s' && ./get_bucket_list_s3.sh %s %s %s %s"
                  % (aws_config_file_path, bucket_name, region, output_file,  prefix))
    if not isinstance(r, int):
        print('err', r)
        return None
    elif r != 0:
        print("error")
        return None
    with open(output_file, 'r+') as file:
        d = xmltodict.parse(file.read())
        s3_bucket_list = S3BucketList(raw=d)
        file.close()
        os.remove(output_file)
        return s3_bucket_list


ret = get_bucket_list(
    aws_config_file_path="./.my-aws-config",
    bucket_name='repos-master-bucket',
    region='us-east-2',
    output_file='my_output.txt',
    prefix="myDirectoryName"
)

if ret:
    print("get bucket list successful\n", (print(i.name) for i in ret.contents))
else:
    print("request failed")
