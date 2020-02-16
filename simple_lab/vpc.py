def create_vpc(ec2_c, cidr_block, lab_tag):
    """
    CidrBlock format '0.0.0.0/16'
    lab_tag is a string
    """
    vpc = ec2_c.create_vpc(CidrBlock=cidr_block)
    vpc.create_tags(Tags=[{
        "Key":"Name",
        "Value": lab_tag
    }])
    vpc.wait_until_availabile()
    return vpc
