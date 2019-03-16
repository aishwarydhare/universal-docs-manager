from udm_python.udms3 import upload_file_to_local

if __name__ == "__main__":
    ret = upload_file_to_local(
        sourceFile="../tmp/samplefile.txt",
        targetFile="../tmp/my_output.txt"
    )
    if ret:
        print("upload successful")
    else:
        print("upload failed")
