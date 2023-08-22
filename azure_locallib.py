# Import the needed credential and management objects from the libraries.
import os

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

