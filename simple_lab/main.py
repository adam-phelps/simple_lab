#!/usr/bin/env python
import boto3
from vpc import create_vpc, create_sg
tag = 'force10'
ec2_r = boto3.resource('ec2')
ec2_c = boto3.resource('ec2')
vpc = create_vpc(ec2_r,'172.19.0.0/24',tag)
sg = create_sg(ec2_c,vpc,tag)
