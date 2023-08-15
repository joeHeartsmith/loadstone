#!/usr/bin/env python3

global aws ; aws = "aws"
global azure ; azure = "azure"
global gcp ; gcp = "gcp"
global oci ; oci = "oci"
locallibs = {aws: True, azure: True, gcp: True, oci: True}

try:
    import aws_locallib
except:
    locallibs[aws] = False

try:
    import azure_locallib
except:
    locallibs[azure] = False

try:
    import gcp_locallib
except:
    locallibs[gcp] = False

try:
    import oci_locallib
except:
    locallibs[oci] = False


test_createvpc = {aws: aws_locallib.test_createvpc, azure:None, gcp:None, oci:None}

test_createvpc[aws](None)
