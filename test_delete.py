import os


def delete_object_from_s3(aws_config_file_path: str, object_to_download: str, bucket_name: str, region: str) -> bool:
    r = os.system("export AWS_CONFIG_FILE='%s' && ./delete_object_s3.sh %s %s %s"
                  % (aws_config_file_path, object_to_download, bucket_name, region))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


ret = delete_object_from_s3(
    aws_config_file_path="./.my-aws-config",
    object_to_download='myDirectoryName/myFileName.xml',
    bucket_name='repos-master-bucket',
    region='us-east-2',
)

if ret:
    print("delete object successful")
else:
    print("upload failed")
