import os


class UDMFileObject:
    modified_at = None
    name = None
    size = None
    content_type = None
    key = None

    def __init__(self, modified_at, name, size, content_type=None, path=None):
        self.modified_at = modified_at
        self.name = name
        self.size = size
        self.content_type = content_type
        self.key = path

    def __str__(self):
        return "fileName:\t%s\nmodified_at:\t%s\nsize:\t%s\nsize:\t%s bytes\npath:\t%s" % (
            self.name, self.modified_at, self.content_type, self.size, self.key)


class S3ObjectMeta(UDMFileObject):
    def __init__(self, modified_at, name, size, content_type=None, path=None):
        super(S3ObjectMeta, self).__init__(modified_at, name, size, content_type, path)

    def __str__(self):
        return super(S3ObjectMeta, self).__str__()


class MySQLObjectMeta(UDMFileObject):
    created_at = None
    extras = None

    def __init__(self, modified_at, name, size, created_at, content_type=None, path=None, extras=""):
        super(MySQLObjectMeta, self).__init__(modified_at, name, size, content_type, path)
        self.extras = extras
        self.created_at = created_at

    def __str__(self):
        s = super(MySQLObjectMeta, self).__str__()
        s += "\ncreated_at:\t" + self.created_at
        s += "\nextra:\t" + self.extras
        return s


class S3BucketList:
    contents: [S3ObjectMeta]
    bucket_name: str
    bucket_size: int
    directory: str
    raw: dict

    def __init__(self, raw: dict):
        self.raw = raw
        self.name = raw['ListBucketResult']['Name']
        self.bucket_size = raw['ListBucketResult']['KeyCount']
        self.directory = raw['ListBucketResult']['prefix'] if 'prefix' in raw['ListBucketResult'] else ""
        self.contents = []
        if isinstance(raw['ListBucketResult']['Contents'], dict):
            tmp = [raw['ListBucketResult']['Contents']]
            raw['ListBucketResult']['Contents'] = tmp
        for item in raw['ListBucketResult']['Contents']:
            s3_obj = S3ObjectMeta(modified_at=item['LastModified'], name=str(item['Key']).split('/')[-1],
                                  size=item['Size'], path=item['Key'])
            self.contents.append(s3_obj)


def parse_response_headers_in_dict(lines):
    d = dict()
    for line in lines:
        sep = line.find(':')
        if sep >= 0:
            key = (line[:sep]).strip()
            val = (line[sep + 1:]).strip()
            d[key] = val
    return d


def delete_object_from_s3(aws_config_file_path: str, input_object: str, bucket_name: str, region: str) -> bool:
    r = os.system("export AWS_CONFIG_FILE='%s' && ../src/delete_object_s3.sh %s %s %s"
                  % (aws_config_file_path, input_object, bucket_name, region))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


def get_bucket_list(aws_config_file_path: str, bucket_name: str, region: str,
                    output_file: str, prefix: str = "") -> S3BucketList:
    import xmltodict
    r = os.system("export AWS_CONFIG_FILE='%s' && ../src/get_bucket_list_s3.sh %s %s %s %s"
                  % (aws_config_file_path, bucket_name, region, output_file, prefix))
    if not isinstance(r, int):
        print('err', r)
        return None
    elif r != 0:
        print("error")
        return None
    with open(output_file, 'r+') as file:
        d = xmltodict.parse(file.read())
        s3_bucket_list = S3BucketList(raw=d)
        file.close()
        os.remove(output_file)
        return s3_bucket_list


def get_object_from_s3(aws_config_file_path: str, object_to_download: str, bucket_name: str, region: str,
                       output_file: str) -> bool:
    r = os.system("export AWS_CONFIG_FILE='%s' && ../src/get_object_s3.sh %s %s %s %s"
                  % (aws_config_file_path, object_to_download, bucket_name, region, output_file))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


def upload_file_to_s3(aws_config_file_path: str, input_object: str, bucket_name: str, region: str, storage_class: str,
                      upload_file_name: str) -> bool:
    r = os.system("export AWS_CONFIG_FILE='%s' && ../src/upload_object_s3.sh %s %s %s %s %s"
                  % (aws_config_file_path, input_object, bucket_name, region, storage_class, upload_file_name))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


def get_object_metadata_from_s3(aws_config_file_path: str, input_object: str, bucket_name: str, region: str,
                                output_file: str) -> S3ObjectMeta:
    r = os.system("export AWS_CONFIG_FILE='%s' && ../src/head_object_s3.sh %s %s %s %s"
                  % (aws_config_file_path, input_object, bucket_name, region, output_file))
    if not isinstance(r, int):
        print('err', r)
        return None
    elif r != 0:
        print("error")
        return None

    obj_meta = None
    with open(output_file, 'r+') as file:
        d = parse_response_headers_in_dict(file.readlines())
        obj_meta = S3ObjectMeta(d['Last-Modified'], input_object.split("/")[-1], d['Content-Length'],
                                d['Content-Type'], input_object)
        file.close()
    os.remove(output_file)
    return obj_meta


def upload_file_to_local(sourceFile: str, targetFile: str) -> bool:
    r = os.system("sh ../src/upload_object_local.sh %s %s" % (sourceFile, targetFile))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False
    return True


def delete_object_from_local(input_object: str) -> bool:
    r = os.system("sh ../src/delete_object_local.sh %s" % input_object)
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


def get_object_metadata_from_local(input_object: str, tmp_output_file: str) -> UDMFileObject:
    r = os.system("sh ../src/head_object_local.sh %s %s" % (input_object, tmp_output_file))
    if not isinstance(r, int):
        print('err', r)
        return None
    elif r != 0:
        print("error")
        return None

    with open(tmp_output_file, 'r+') as file:
        d = parse_response_headers_in_dict(file.readlines())
        obj_meta = UDMFileObject(
            modified_at=d['LastModified'],
            name=d['Name'],
            size=d['Size'],
            content_type=d['ContentType'],
            path=d['Path']
        )
        file.close()
    os.remove(tmp_output_file)
    return obj_meta


def upload_file_to_mysql(host: str, username: str, password: str, db_name: str, input_object: str, tmp_output_file: str,
                         str_extras="") -> bool:
    r = os.system("sh ../src/upload_object_mysql.sh %s %s %s %s %s %s %s" \
                  % (host, username, password, db_name, input_object, tmp_output_file, str_extras))
    if not isinstance(r, int):
        print('err', r)
        return False
    else:
        with open(tmp_output_file, 'r') as file:
            print("stored in mysql table with primary key:", file.read())
            file.close()
            os.remove(tmp_output_file)
            return True


def get_object_from_mysql(host: str, username: str, password: str, db_name: str, row_id: str, output_file: str) -> bool:
    r = os.system("../src/get_object_mysql.sh %s %s %s %s %s %s"
                  % (host, username, password, db_name, row_id, output_file))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False

    return True


def delete_object_from_mysql(host: str, username: str, password: str, db_name: str, row_id: str) -> bool:
    r = os.system("sh ../src/delete_object_mysql.sh %s %s %s %s %s" % (host, username, password, db_name, row_id))
    if not isinstance(r, int):
        print('err', r)
        return False
    elif r != 0:
        print("error")
        return False
    return True


def get_object_metadata_from_mysql(host: str, username: str, password: str, db_name: str, row_id: str,
                                   tmp_output_file: str) -> MySQLObjectMeta:
    r = os.system(
        "sh ../src/head_object_mysql.sh %s %s %s %s %s %s" % (host, username, password, db_name, row_id, tmp_output_file))
    if not isinstance(r, int):
        print('err', r)
        return None
    elif r != 0:
        print("error")
        return None

    with open(tmp_output_file, 'r+') as file:
        d = parse_response_headers_in_dict(file.readlines())
        obj_meta = MySQLObjectMeta(
            modified_at=d['LastModified'],
            name=d['Name'],
            size=d['Size'],
            created_at=d['CreatedAt'],
            content_type=d['ContentType'],
            extras=d['Extras']
        )
        file.close()
        os.remove(tmp_output_file)
        return obj_meta
