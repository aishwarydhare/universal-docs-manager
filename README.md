# Universal Docs Manager

- Create, Delete, Read/Load, Get Meta-data of Files
- Supports: Local Disk, MySQL and AWS S3
- Purely written in Shell
- Work with any programming language i.e. Python, JavaScript, C, Go, JAVA and etc
- Compatible in All UNIX based OS
- Work with Windows 10 using [Ubuntu Application](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab)

## Source Files 

##### Upload, download (get), head (meta-data) or delete files on AWS
 
- upload_object_s3.sh
- get_object_s3.sh
- delete_object_s3.sh
- head_object_s3.sh

##### List, head (meta-data) or delete AWS Buckets (files)
- get_bucket_list_s3.sh
- head_bucket_s3.sh
- delete_bucket_s3.sh

##### Save, download (get), head (meta-data) or delete files in local system
- upload_object_local.sh
- head_object_local.sh
- delete_object_local.sh

##### Store, download (get), head (meta-data) or delete files in MySQL Database
- upload_object_mysql.sh
- get_object_mysql.sh
- head_object_mysql.sh
- delete_object_mysql.sh


## Tests

### Testing Shell Scripts

##### Test S3 operations

using test files provided in directory ./shell_test_s3/

> Note -  
> File management on S3 requires `.my-aws-config` config file to be present in root directory with AWS Credentials. Check `.my-aws-config-sample` file for more details  
>

- test_upload.sh
- test_get.sh
- test_head.sh
- test_delete.sh
- test_get_bucket_list.sh
- test_bucket_head.sh
- test_bucket_delete.sh

##### Test Local file system operations

use test files provided in directory shell_test_local/

- test_upload.sh
- test_get_meta.sh
- test_delete.sh

##### Test MySQL operations

use test files provided in directory shell_test_mysql/

> Note -
>
> File management on S3 requires mysql-server and mysql-client to be installed on system  
> Tested OK on MySQL v8.0.15

- test_upload.sh
- test_load.sh
- test_get_meta.sh
- test_delete.sh


### Working with Python

#### Wrapper Library: udm_python/udm.py

In **udm.py**, python methods uses shell scripts to execute file management operations.  
Python's `os.system()` is used to execute the commands and shell scripts in a system's subshell.
   
> Note - 
> **Please use python 3.7** as the provided library udm.py uses parameter hints and method return type hints   

##### Python: Test S3 operations

> Note -
> `get_bucket_list()` method used for fetching all items in a provided S3 bucket has dependency to **[xmltodict](https://pypi.org/project/xmltodict/)** library, install it with `pip install xmltodict`

use test files provided in directory python_test_s3/

- test_s3_upload.py
- test_s3_get.py
- test_s3_delete.py
- test_s3_head.py
- test_s3_bucket_list.py   

##### Python: Test Local file operations

use test files provided in directory python_test_local/

- test_local_upload.py
- test_local_head.py
- test_local_delete.py

##### Python: Test MySQL operations

use test files provided in directory python_test_mysql/

- test_mysql_delete.py
- test_mysql_get.py
- test_mysql_head.py
- test_mysql_upload.py


## Extending with other programming languages

Similar to provided implementation in python, all other programming languages can be used.
  
For instance, a udm.js javascript library can be written using javascript where **[shelljs](https://github.com/shelljs/shelljs)** can be used to execute commands in shell scripts and system's subshell.
   


## Extending with other storage systems

- Similar to provided implementation in S3, services by Azure, Akamai can be used
- Similar to provided implementation in MySQL, other SQL or NoSQL databases can be used



--
--



 