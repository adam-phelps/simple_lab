# Simple_Lab (boto3)

![Lab Visual](imgs/botolab.png?raw=true "Boto3 Lab")

Quickily and easily provision EC2 instances in AWS! This is very helpful for quickly mocking up projects requiring servers in Linux Academy lab without worrying about leaving instances running.

## Installation

Git clone the repo to a local directory.
Edit the json file:
```{
    "lab_tag": "mylab10",
    "ports": {
            "ssh": "22"
        },
    "networks": {
            "vpc-lab": "172.19.0.0/16",
            "public-sub-lab": "172.19.1.0/24"
        },
    "keys": {
        "ssh-key": "key-pair-lab"
        },
    "instance_info": {
        "ImageId": "ami-0a887e401f7654935",
        "InstanceType": "t2.micro",
        "KeyName": "key-pair-lab",
        "amount": "2"
    }
}```

## Usage

Edit this file as needed to create a dynamic lab setup.


## Helpers folder

Storage for misc scripts and one-liners that are helpful for troubleshooting edge cases.
