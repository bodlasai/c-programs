import boto3
iam = boto3.client('iam')
response = iam.create_user(
    UserName='sai-user'
)
print(response)
#list the users in account
listusers = iam.get_paginator('list_users')
for response in listusers.paginate():
    print(response)
iam.update_user(
    UserName='sai-user',
    NewUserName='new_user_sai'
)
iam.delete_user(
    UserName='new_user_sai'
)
ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami_number',
    # MinCount=1,
    # MaxCount=1,
    InstanceType='t2.micro',
)
print(instance[0].id)

