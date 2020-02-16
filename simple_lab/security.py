def create_key_pair(ec2_c,my_key):
    try:
        response = ec2_c.create_key_pair(KeyName=my_key)
        with open(my_key + ".pem","w") as f:
            f.write(response['KeyMaterial'])
        return response
    except:
        response = ec2_c.describe_key_pairs(KeyNames=[my_key])
        return response
