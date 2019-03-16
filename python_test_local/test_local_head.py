from udm_python.udms3 import get_object_metadata_from_local

if __name__ == "__main__":
    ret = get_object_metadata_from_local(
        input_object="../tmp/samplefile.txt",
        tmp_output_file="../tmp/my_output.txt"
    )
    if ret:
        print("head successful")
        print(ret)
    else:
        print("head failed")
