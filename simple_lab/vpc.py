def create_vpc(ec2_r, cidr_block, lab_tag):
    """
    CidrBlock format '0.0.0.0/16'
    lab_tag is a string
    """
    vpc = ec2_r.create_vpc(CidrBlock=cidr_block)
    vpc.create_tags(Tags=[{
        "Key":"Name",
        "Value": lab_tag
    }])
    vpc.wait_until_available()
    return vpc

def create_sg(ec2_c,vpc_id, lab_tag):
    sg = ec2_c.create_security_group(
        GroupName=lab_tag,
        Description=lab_tag,
        VpcId=vpc_id.id)
    return sg
