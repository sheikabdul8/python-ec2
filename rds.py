#!/usr/bin/python3


import boto3
import csv

region='us-east-1'
aws_con=boto3.session.Session(profile_name="root")
aws_rds=boto3.client('rds',region_name=region)
aws_s3=aws_con.resource('s3')


csv_obj=open("rds_inventory.csv","w",newline='')
csv_wrt=csv.writer(csv_obj)
csv_wrt.writerow(["Status", "Class", "EngineType", "AvailabilityZone", "ARN", "StorageType"])

for rds1 in aws_rds.describe_db_instances()['DBInstances']:
    
        print(rds1['DBInstanceStatus'], rds1['DBInstanceClass'], rds1['Engine'], rds1['AvailabilityZone'], rds1['DBInstanceArn'], rds1['StorageType'])
        csv_wrt.writerow([rds1['DBInstanceStatus'],rds1['DBInstanceClass'],rds1['Engine'],rds1['AvailabilityZone'],rds1['DBInstanceArn'],rds1['StorageType']])

         

csv_obj.close()

aws_s3.meta.client.upload_file(Filename='rds_inventory.csv', Bucket='sheik627811', Key='rds_inventory.csv')
