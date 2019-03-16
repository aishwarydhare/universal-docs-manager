from udm_python.udms3 import delete_object_from_s3

if __name__ == "__main__":
    ret = delete_object_from_s3(
        aws_config_file_path="../.my-aws-config",
        input_object='myDirectoryName/myFileName.xml',
        bucket_name='repos-master-bucket',
        region='us-east-2',
    )

    if ret:
        print("delete object successful")
    else:
        print("request failed")
