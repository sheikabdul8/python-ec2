#!/usr/bin/python3

import boto3
import csv

aws_con=boto3.session.Session(profile_name="root")
aws_cli=aws_con.client('ec2')
aws_res=aws_con.resource('ec2')

aws_s3=aws_con.resource('s3')


count=1
csv_obj=open("ec2_instances.csv","w",newline='')
csv_wr=csv.writer(csv_obj)
csv_wr.writerow(["sl.no", "ImageId", "InstanceId", "Type", "LaunchTime", "PrivateIp", "PublicIp", "State", "SubnetId", "VpcId"])

for aws_ins in aws_cli.describe_instances()['Reservations']:
    for aws_details in aws_ins['Instances']:
        print(count, aws_details['ImageId'], aws_details['InstanceId'], aws_details['InstanceType'], aws_details['LaunchTime'], aws_details['PrivateIpAddress'], aws_details['PublicIpAddress'], aws_details['State']['Name'], aws_details['SubnetId'], aws_details['VpcId'])
        csv_wr.writerow([count,aws_details['ImageId'],aws_details['InstanceId'],aws_details['InstanceType'],aws_details['LaunchTime'],aws_details['PrivateIpAddress'],aws_details['PublicIpAddress'],aws_details['State']['Name'],aws_details['SubnetId'],aws_details['VpcId'] ])
        count+=1

csv_obj.close()



aws_s3.meta.client.upload_file(Filename="ec2_instances.csv", Bucket = 'sheik627811', Key='ec2_instances.csv')
