# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .restore_request_py3 import RestoreRequest


class IaasVMRestoreRequest(RestoreRequest):
    """IaaS VM workload-specific restore.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_point_id: ID of the backup copy to be recovered.
    :type recovery_point_id: str
    :param recovery_type: Type of this recovery. Possible values include:
     'Invalid', 'OriginalLocation', 'AlternateLocation', 'RestoreDisks'
    :type recovery_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryType
    :param source_resource_id: Fully qualified ARM ID of the VM which is being
     recovered.
    :type source_resource_id: str
    :param target_virtual_machine_id: This is the complete ARM Id of the VM
     that will be created.
     For e.g.
     /subscriptions/{subId}/resourcegroups/{rg}/provider/Microsoft.Compute/virtualmachines/{vm}
    :type target_virtual_machine_id: str
    :param target_resource_group_id: This is the ARM Id of the resource group
     that you want to create for this Virtual machine and other artifacts.
     For e.g. /subscriptions/{subId}/resourcegroups/{rg}
    :type target_resource_group_id: str
    :param storage_account_id: Fully qualified ARM ID of the storage account
     to which the VM has to be restored.
    :type storage_account_id: str
    :param virtual_network_id: This is the virtual network Id of the vnet that
     will be attached to the virtual machine.
     User will be validated for join action permissions in the linked access.
    :type virtual_network_id: str
    :param subnet_id: Subnet ID, is the subnet ID associated with the to be
     restored VM. For Classic VMs it would be
     {VnetID}/Subnet/{SubnetName} and, for the Azure Resource Manager VMs it
     would be ARM resource ID used to represent
     the subnet.
    :type subnet_id: str
    :param target_domain_name_id: Fully qualified ARM ID of the domain name to
     be associated to the VM being restored. This applies only to Classic
     Virtual Machines.
    :type target_domain_name_id: str
    :param region: Region in which the virtual machine is restored.
    :type region: str
    :param affinity_group: Affinity group associated to VM to be restored.
     Used only for Classic Compute Virtual Machines.
    :type affinity_group: str
    :param create_new_cloud_service: Should a new cloud service be created
     while restoring the VM. If this is false, VM will be restored to the same
     cloud service as it was at the time of backup.
    :type create_new_cloud_service: bool
    :param original_storage_account_option: Original Storage Account Option
    :type original_storage_account_option: bool
    :param encryption_details: Details needed if the VM was encrypted at the
     time of backup.
    :type encryption_details:
     ~azure.mgmt.recoveryservicesbackup.models.EncryptionDetails
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_id': {'key': 'recoveryPointId', 'type': 'str'},
        'recovery_type': {'key': 'recoveryType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'target_virtual_machine_id': {'key': 'targetVirtualMachineId', 'type': 'str'},
        'target_resource_group_id': {'key': 'targetResourceGroupId', 'type': 'str'},
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'virtual_network_id': {'key': 'virtualNetworkId', 'type': 'str'},
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
        'target_domain_name_id': {'key': 'targetDomainNameId', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
        'affinity_group': {'key': 'affinityGroup', 'type': 'str'},
        'create_new_cloud_service': {'key': 'createNewCloudService', 'type': 'bool'},
        'original_storage_account_option': {'key': 'originalStorageAccountOption', 'type': 'bool'},
        'encryption_details': {'key': 'encryptionDetails', 'type': 'EncryptionDetails'},
    }

    def __init__(self, *, recovery_point_id: str=None, recovery_type=None, source_resource_id: str=None, target_virtual_machine_id: str=None, target_resource_group_id: str=None, storage_account_id: str=None, virtual_network_id: str=None, subnet_id: str=None, target_domain_name_id: str=None, region: str=None, affinity_group: str=None, create_new_cloud_service: bool=None, original_storage_account_option: bool=None, encryption_details=None, **kwargs) -> None:
        super(IaasVMRestoreRequest, self).__init__(**kwargs)
        self.recovery_point_id = recovery_point_id
        self.recovery_type = recovery_type
        self.source_resource_id = source_resource_id
        self.target_virtual_machine_id = target_virtual_machine_id
        self.target_resource_group_id = target_resource_group_id
        self.storage_account_id = storage_account_id
        self.virtual_network_id = virtual_network_id
        self.subnet_id = subnet_id
        self.target_domain_name_id = target_domain_name_id
        self.region = region
        self.affinity_group = affinity_group
        self.create_new_cloud_service = create_new_cloud_service
        self.original_storage_account_option = original_storage_account_option
        self.encryption_details = encryption_details
        self.object_type = 'IaasVMRestoreRequest'
