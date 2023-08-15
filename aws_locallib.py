import boto3

def test_createvpc(invar=None):
    client = boto3.client('ec2')
    client.create_vpc(CidrBlock="192.168.19.0/24")
