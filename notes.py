#!/usr/bin/env python3

import aws_locallib

print(awsvar1)

global lib_boto3 ; lib_boto3 = False

"""
try:
   import boto3
   lib_boto3 = True
except:
   print("IMPORT: no boto3")
"""

def aws_func(invar=None):
   if lib_boto3 == False:
       #raise Exception('No boto3')
       print('no boto3')
   else:
        print("the aws version was called with " + str(invar) + ".")


def azure_func(invar=None):
   print("the azure version was called with " + str(invar) + ".")

global aws ; aws = "aws"
global azure ; azure = "azure"

basic_func = {aws: aws_func, azure:azure_func}

basic_func[aws]("TEST VALUE")
basic_func[azure]("TEST VALUE")


