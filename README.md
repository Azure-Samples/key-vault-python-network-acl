---
services: key-vault
platforms: python
author: schaabs
---

***DISCLAIMER: The samples in this repo are for `azure-mgmt-keyvault` v1 (1.x). For the latest version of `azure-mgmt-keyvault`, please visit the [`azure-sdk-for-python` repository](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/keyvault/azure-mgmt-keyvault). This repo is archived since a new version of `azure-mgmt-keyvault` has become stable.***

# Managing network access to a key vault using the Azure Python SDK

This Sample repo includes sample code that demonstrates managing network access to a key vault through VNET and IP ACLs using the Azure Python SDK.

## Samples in this repo
* network_acl_sample.py
  * create_vault_with_network --Creates a key vault with network access limited by a NetworkRuleSet


## Running The samples
1. If you don't already have it, [install Python](https://www.python.org/downloads/).

2. We recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to run this example, but it's not mandatory. You can initialize a virtual environment this way:

    ```
    pip install virtualenv
    virtualenv mytestenv
    cd mytestenv
    source bin/activate
    ```

3. Clone the repository.

    ```
    git clone https://github.com/Azure-Samples/key-vault-python-network-acl.git
    ```

4. Install the dependencies using pip.

    ```
    cd key-vault-python-network-acl
    pip install -r requirements.txt
    ```

5. Create an Azure service principal, using
[Azure CLI](http://azure.microsoft.com/documentation/articles/resource-group-authenticate-service-principal-cli/),
[PowerShell](http://azure.microsoft.com/documentation/articles/resource-group-authenticate-service-principal/)
or [Azure Portal](http://azure.microsoft.com/documentation/articles/resource-group-create-service-principal-portal/).

6. Export these environment variables into your current shell.

    on Linux and Mac
    ```
    export AZURE_TENANT_ID={your tenant id}
    export AZURE_CLIENT_ID={your service principal AppID}
    export AZURE_CLIENT_OID={your service principal OID}
    export AZURE_CLIENT_SECRET={your application key}
    export AZURE_SUBSCRIPTION_ID={your subscription id}
    ```

    on Windows
    ```
    set AZURE_TENANT_ID={your tenant id}
    set AZURE_CLIENT_ID={your service principal AppID}
    set AZURE_CLIENT_OID={your service principal OID}
    set AZURE_CLIENT_SECRET={your application key}
    set AZURE_SUBSCRIPTION_ID={your subscription id}
    ```

7. Run the samples, optionally specifying a space delimited list of specific samples to run.

    ```
    python network_acl_sample.py
    ```

## Minimum Requirements
Python 2.7, 3.3, or 3.4.
To install Python, please go to https://www.python.org/downloads/

## More information

* What is Key Vault? - https://docs.microsoft.com/en-us/azure/key-vault/key-vault-whatis
* Get started with Azure Key Vault - https://docs.microsoft.com/en-us/azure/key-vault/key-vault-get-started
* Azure Key Vault General Documentation - https://docs.microsoft.com/en-us/azure/key-vault/
* Azure Key Vault REST API Reference - https://docs.microsoft.com/en-us/rest/api/keyvault/
* Azure SDK for Python Documentation - https://docs.microsoft.com/en-us/python/api/overview/azure/key-vault?view=azure-python
* Azure Active Directory Documenation - https://docs.microsoft.com/en-us/azure/active-directory/

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information
see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com)
with any additional questions or comments.
