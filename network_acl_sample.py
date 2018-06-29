# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# This script expects that the following environment vars are set
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Service Principal AppId
# AZURE_CLIENT_OID: with your Azure Active Directory Service Principal object id
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Key
# AZURE_SUBSCRIPTION_ID: with your Azure Subscription Id
#

from util import KeyVaultSampleBase, get_name, keyvaultsample
from msrestazure.azure_active_directory import ServicePrincipalCredentials
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.keyvault.models import AccessPolicyEntry, VaultProperties, Sku, KeyPermissions, SecretPermissions, \
    CertificatePermissions, StoragePermissions, Permissions, VaultCreateOrUpdateParameters, NetworkRuleSet, \
    NetworkRuleAction, VirtualNetworkRule, IPRule, NetworkRuleBypassOptions

SECRET_PERMISSIONS_ALL = [perm for perm in SecretPermissions]
KEY_PERMISSIONS_ALL = [perm for perm in KeyPermissions]
CERTIFICATE_PERMISSIONS_ALL = [perm for perm in CertificatePermissions]
STORAGE_PERMISSIONS_ALL = [perm for perm in StoragePermissions]


class NetworkAclSample(KeyVaultSampleBase):
    def __init__(self, config=None):
        super(NetworkAclSample, self).__init__(config=config)

        creds = ServicePrincipalCredentials(client_id=self.config.client_id,
                                            secret=self.config.client_secret,
                                            tenant=self.config.tenant_id)

        self.mgmt_client = KeyVaultManagementClient(credentials=creds,
                                                    subscription_id=self.config.subscription_id)

        self.vault = None

    def run_all_samples(self):
        self.create_vault_with_network()

    @keyvaultsample
    def create_vault_with_network(self):
        """
        Creates a key vault with network access limited by a NetworkRuleSet
        """
        vault_name = get_name('vault')

        # setup vault permissions for the access policy for the sample service principle
        permissions = Permissions(keys=KEY_PERMISSIONS_ALL,
                                  secrets=SECRET_PERMISSIONS_ALL,
                                  certificates=CERTIFICATE_PERMISSIONS_ALL,
                                  storage=STORAGE_PERMISSIONS_ALL)

        policy = AccessPolicyEntry(tenant_id=self.config.tenant_id,
                                   object_id=self.config.client_oid,
                                   permissions=permissions)

        # Network ACL definitions
        # The only action supported for virtual network and IP rules is "allow".
        # To deny an address, set the default action to 'deny' and do not explicitly allow the address.
        network_acls = NetworkRuleSet(
            # allow bypass of network ACL rules by other azure services. Valid values are azure_services or none
            bypass=NetworkRuleBypassOptions.azure_services,
            # the action to take if access attempt doesn't match any rule.  Valid values are allow or deny
            default_action=NetworkRuleAction.deny,
            # IP rules (allowed IPv4 addresses / ranges)
            ip_rules=[IPRule(value='0.0.0.0/0')],  #  Allow access from a IP address range
            # Virtual network rules(Allows access to Azure Virtual Networks by their Azure Resource ID)
            virtual_network_rules=[
                # To specifically allow access to a vnet, uncomment the line below and replace the id with the correct
                # resource id for your vnet
                # VirtualNetworkRule(id='/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1')
            ]
        )

        properties = VaultProperties(tenant_id=self.config.tenant_id,
                                     sku=Sku(name='standard'),
                                     access_policies=[policy],
                                     network_acls=network_acls)

        parameters = VaultCreateOrUpdateParameters(location=self.config.location,
                                                   properties=properties)
        parameters.properties.enabled_for_deployment = True
        parameters.properties.enabled_for_disk_encryption = True
        parameters.properties.enabled_for_template_deployment = True

        print('creating vault {}'.format(vault_name))

        self.vault = self.mgmt_client.vaults.create_or_update(resource_group_name=self.config.group_name,
                                                              vault_name=vault_name,
                                                              parameters=parameters).result()


if __name__ == "__main__":
    NetworkAclSample().create_vault_with_network()
