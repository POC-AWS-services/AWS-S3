__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"


#The download_file method accepts the names of the bucket and object to download and the filename to save the file to.

import boto3

s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

#The download_fileobj method accepts a writeable file-like object. The file object must be opened in binary mode, not text mode.

s3 = boto3.client('s3')
with open('FILE_NAME', 'wb') as f:
    s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)
