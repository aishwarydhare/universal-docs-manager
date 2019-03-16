from udm_python.udms3 import upload_file_to_mysql

if __name__ == "__main__":
    ret = upload_file_to_mysql(
        host="127.0.0.1",
        username="root",
        password="root",
        db_name="temp",
        input_object="../tmp/samplefile.txt",
        tmp_output_file="../tmp/tmp.txt",
        str_extras="my_custom_extra_data"
    )
    if ret:
        print("upload successful")
    else:
        print("upload failed")
