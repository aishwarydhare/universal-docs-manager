import os


def upload_file_to_s3(aws_config_file_path: str, file_to_upload: str, bucket_name: str, region: str, storage_class: str,
                      upload_file_name: str) -> bool:
    r = os.system("export AWS_CONFIG_FILE='%s' && ./upload_object_s3.sh %s %s %s %s %s"
                  % (aws_config_file_path, file_to_upload, bucket_name, region, storage_class, upload_file_name))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


ret = upload_file_to_s3(
    aws_config_file_path="./.my-aws-config",
    file_to_upload='samplefile.xml',
    bucket_name='repos-master-bucket',
    region='us-east-2',
    storage_class='STANDARD',
    upload_file_name='myDirectoryName/myFileName.xml'
)

if ret:
    print("upload successful")
else:
    print("upload failed")
