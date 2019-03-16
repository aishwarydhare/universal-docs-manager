from udm_python.udms3 import get_object_metadata_from_mysql

if __name__ == "__main__":
    ret = get_object_metadata_from_mysql(
        host="127.0.0.1",
        username="root",
        password="root",
        db_name="temp",
        row_id="38",
        tmp_output_file="../tmp/tmp.txt"
    )
    if ret:
        print("head successful")
        print(ret)
    else:
        print("head failed")
