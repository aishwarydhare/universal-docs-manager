from udm_python.udm import delete_object_from_local

if __name__ == "__main__":
    ret = delete_object_from_local(
        input_object="../tmp/tmp.txt",
    )
    if ret:
        print("delete successful")
    else:
        print("delete failed")
