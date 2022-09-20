import json
import os
import pysftp as sftp
import urllib.parse
import boto3

FTP_HOST = "valueFTP_HOST"
FTP_USER = "valueFTP_USER"
FTP_PASS = "123456"
FTP_PORT = 22
FTP_PATH = '/path/dir/root/'
#Ignorando certificado
cnopts = sftp.CnOpts()
cnopts.hostkeys = None

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    global FTP_HOST
    global FTP_USER
    global FTP_PASS
    global FTP_PORT
    global cnopts
    global sftp
    
    if event and event['Records']:
        for record in event['Records']:
            sourcebucket = record['s3']['bucket']['name']
            sourcekey = record['s3']['object']['key']
            print("Mostrando SourceBucket " + sourcebucket)
            print("Mostrando SourceKey " + sourcekey)
            
            #Download the file to /tmp/ folder
            filename = os.path.basename(sourcekey)
            download_path = '/tmp/'+ filename
            print(download_path)
            s3.download_file(sourcebucket, sourcekey, download_path)
            
            os.chdir("/tmp/")
            
            with sftp.Connection(host=FTP_HOST, port=FTP_PORT, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
                print("Connection succesfully stablished ... ")
                sftp.cwd(FTP_PATH)  # Entrando no diretorio
                sftp.put(filename)
            os.remove(filename)
