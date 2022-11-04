#!/usr/bin/python3.9

import boto3
import json

aws_con=boto3.session.Session(profile_name="ansible-user")
aws_cli=aws_con.client('ec2')
aws_res=aws_con.resource('ec2')


count=1

for aws_ins in aws_cli.describe_instances()['Reservations']:
    for aws_details in aws_ins['Instances']:
        print(count, aws_details['ImageId'], aws_details['InstanceId'], aws_details['InstanceType'], aws_details['PrivateIpAddress'], aws_details['PublicIpAddress'],  aws_details['SubnetId'], aws_details['VpcId'])
        count+=1


