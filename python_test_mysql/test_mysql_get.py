from udm_python.udm import get_object_from_mysql

if __name__ == "__main__":
    ret = get_object_from_mysql(
        host="127.0.0.1",
        username="root",
        password="root",
        db_name="temp",
        row_id="31",
        output_file="../tmp/tmp.txt"
    )
    if ret:
        print("load successful")
    else:
        print("load failed")
