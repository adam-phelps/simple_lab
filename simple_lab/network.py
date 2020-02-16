def create_vpc(ec2_r, cidr_block, lab_tag):
    vpc = ec2_r.create_vpc(CidrBlock=cidr_block)
    vpc.create_tags(Tags=[{
        "Key":"Name",
        "Value": lab_tag
    }])
    vpc.wait_until_available()
    return vpc

def create_internet_gateway(ec2_c,vpc):
    igw = ec2_c.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGateway=igw.id)
    return igw

def create_route_table(vpc, igw):
    rt_table = vpc.create_route_table()
    rt_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw.id
    )
    return rt_table

def create_subnet(ec2_c,vpc,rt_table,networks,lab_tag):
    subnet = ec2_c.create_subnet(CidrBlock=networks['vpc'+'-'+lab_tag],VpcId=vpc.id)
    rt_table.associate_with_subnet(SubnetId=subnet.id)
    return subnet

def create_security_group(ec2_c,vpc, lab_tag):
    sg = ec2_c.create_security_group(
        GroupName=lab_tag,
        Description=lab_tag,
        VpcId=vpc.id)
    return sg

def authorize_security_group_ingress(ec2_c,sg_id,port):
    try:
        ec2_c.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[{
                'IpProtocol':'tcp',
                'FromPort': port,
                'ToPort': port,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }]
            )
    except Exception as e:
        print(e)
    return 0
