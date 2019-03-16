from udms3 import upload_file_to_s3

if __name__ == "__main__":
    ret = upload_file_to_s3(
        aws_config_file_path="../.my-aws-config",
        file_to_upload='../tmp/myfile.txt',
        bucket_name='repos-master-bucket',
        region='us-east-2',
        storage_class='STANDARD',
        upload_file_name='myDirectoryName/myFileName.xml'
    )

    if ret:
        print("upload successful")
    else:
        print("upload failed")
