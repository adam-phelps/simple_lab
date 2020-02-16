def create_key_pairp(ec2_c,my_key):
    try:
        response = ec2.create_key_pair(KeyName=my_key)
        with open(my_key + ".pem","w") as f:
            f.write(response['KeyMaterial'])
        return response
    except:
        response = ec2.describe_key_pairs(KeyNames=[my_key])
        return response
