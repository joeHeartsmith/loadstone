import boto3

def get_infrax_info(invar=None):
    client = boto3.client('ec2')
    print(client.describe_vpcs())

# TODO: add find_vpc_by_X functions (i.e. by address, name, options, etc)

def test_createvpc(address):
    client = boto3.client('ec2')
    client.create_vpc(CidrBlock=address)

def test_deletevpc(name):
    client = boto3.client('ec2')
    client.delete_vpc(VpcId=name)
