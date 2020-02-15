#!/usr/bin/env python
import boto3
from vpc import create_vpc
tag = 'force10'
ec2_c = boto3.client('ec2')
vpc = create_vpc(ec2_c,'172.19.0.0/24',tag)