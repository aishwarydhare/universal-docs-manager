import os


def get_object_from_s3(aws_config_file_path: str, object_to_download: str, bucket_name: str, region: str, output_file: str) -> bool:
    r = os.system("export AWS_CONFIG_FILE='%s' && ./get_object_s3.sh %s %s %s %s"
                  % (aws_config_file_path, object_to_download, bucket_name, region, output_file))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


ret = get_object_from_s3(
    aws_config_file_path="./.my-aws-config",
    object_to_download='myDirectoryName/myFileName.xml',
    bucket_name='repos-master-bucket',
    region='us-east-2',
    output_file='my_output.xml'
)

if ret:
    print("get object successful")
else:
    print("upload failed")
