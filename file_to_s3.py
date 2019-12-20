from boto3.session import Session
import os

def base_config():

    access_key = "your access_key"
    secret_key = "your secret_key"
    # url = "http://eos-beijing-1.cmecloud.cn"
    session = Session(access_key, secret_key)
    s3_client = session.client('s3')  # , endpoint_url=url

    return s3_client

def make_bucket(s3_client):

    s3_client.create_bucket(Bucket="mjdev-wallpaper1",ACL='public-read')
    print ([bucket['Name'] for bucket in s3_client.list_buckets()['Buckets']])

def upload_file(s3_client):

    # 目录名称
    dir_name = 'Abstract'

    fileList = os.listdir(r"/Users/mjdev/Desktop/save_source_project/" + dir_name)

    for fileName in fileList:  # 遍历文件夹中所有文件
        print(fileName)
        resp = s3_client.put_object(
            Bucket="mjdev-wallpaper1",
            Key="static/test/" + fileName,
            Body=open("/Users/mjdev/Desktop/save_source_project/" + dir_name + "/" + fileName, 'rb').read()
        )


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用

    s3_client = base_config() #连接S3
    make_bucket(s3_client) #创建文件夹
    upload_file(s3_client) #上传资源
