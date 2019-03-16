from udms3 import get_bucket_list

if __name__ == "__main__":
    ret = get_bucket_list(
        aws_config_file_path="../.my-aws-config",
        bucket_name='repos-master-bucket',
        region='us-east-2',
        output_file='../tmp/my_output.txt',
        prefix="myDirectoryName"
    )

    if ret:
        print("get bucket list successful, contents are:-")
        for i in ret.contents:
            print("\t", i.name, i.size, "bytes", ", full path:", i.key, " last modified at:", i.modified_at)
    else:
        print("request failed")
