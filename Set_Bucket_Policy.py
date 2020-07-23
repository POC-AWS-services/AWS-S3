__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"


# Imports
import boto3
import json


# Retrieve the policy of the specified bucket
s3 = boto3.client('s3')
result = s3.get_bucket_policy(Bucket='BUCKET_NAME')
print(result['Policy'])

# Create a bucket policy
bucket_name = 'BUCKET_NAME'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

# Delete a bucket's policy
s3 = boto3.client('s3')
s3.delete_bucket_policy(Bucket='BUCKET_NAME')