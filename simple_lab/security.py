def create_key_pair(ec2_c,my_key):
    try:
        response = ec2_c.create_key_pair(KeyName=my_key)
        with open(my_key + ".pem","w") as f:
            f.write(response['KeyMaterial'])
        return response
    except:
        print("Key {} already exists.".format(my_key))
        return 0
