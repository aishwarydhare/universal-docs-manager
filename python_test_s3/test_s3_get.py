from udm_python.udms3 import get_object_from_s3

if __name__ == "__main__":
    ret = get_object_from_s3(
        aws_config_file_path="../.my-aws-config",
        object_to_download='myDirectoryName/myTwoFileName.xml',
        bucket_name='repos-master-bucket',
        region='us-east-2',
        output_file='../tmp/my_output.xml'
    )

    if ret:
        print("get object successful")
    else:
        print("request failed")
