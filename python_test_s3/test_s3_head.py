from udm_python.udm import get_object_metadata_from_s3

if __name__ == "__main__":
    ret = get_object_metadata_from_s3(
        aws_config_file_path="../.my-aws-config",
        input_object='myDirectoryName/myTwoFileName.xml',
        bucket_name='sample-bucket',
        region='us-east-2',
        output_file='../tmp/my_output_file.txt'
    )

    if ret:
        print("get object metadata successful\n%s" % ret)
    else:
        print("request failed")
