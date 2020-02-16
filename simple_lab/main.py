#!/usr/bin/env python
import boto3
from network import create_route,create_vpc, create_security_group, authorize_security_group_ingress,create_internet_gateway
from security import create_key_pair
from compute import create_instances

# TODO: Import these from a JSON file in the userspace
lab_tag = 'force10'

ports = {
    'ssh':'22'
    }
networks = {
    'vpc'+'-'+lab_tag:'172.19.0.0/16',
    'public-sub'+'-'+lab_tag:'172.19.1.0/24'
    }
keys = {
    'ssh-key': 'key-pair-' + lab_tag
}

instance_info = {
    'ImageId'='ami-0a887e401f7654935',
    'InstanceType'='t2.micro',
    'KeyName'=keys['ssh-key']
}

ec2_r = boto3.resource('ec2')
ec2_c = boto3.resource('ec2')
create_key_pair(ec2_c,vpc,lab_tag)
vpc = create_vpc(ec2_r, networks['public'],lab_tag)
sg = create_security_group(ec2_c,vpc,lab_tag)
authorize_security_group_ingress(ec2_c,sg,ports['ssh'])
igw = create_internet_gateway(ec2_c,vpc)
rt_table = create_route_table(ec2_c,vpc)
sub = create_subnet(ec2_r,vpc,rt_table,networks,lab_tag)
instance = create_instances(ec2_c,sg,sub,lab_tag,instance_info,'Public-Linux')
print(instance[0].public_ip_address)
