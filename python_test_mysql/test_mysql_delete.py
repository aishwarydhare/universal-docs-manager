from udm_python.udms3 import delete_object_from_mysql

if __name__ == "__main__":
    ret = delete_object_from_mysql(
        host="127.0.0.1",
        username="root",
        password="root",
        db_name="temp",
        row_id="31"
    )
    if ret:
        print("delete successful")
    else:
        print("delete failed")
