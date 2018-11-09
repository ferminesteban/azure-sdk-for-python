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

from .protection_policy import ProtectionPolicy


class AzureVmWorkloadProtectionPolicy(ProtectionPolicy):
    """Azure VM (Mercury) workload-specific backup policy.

    All required parameters must be populated in order to send to Azure.

    :param protected_items_count: Number of items associated with this policy.
    :type protected_items_count: int
    :param backup_management_type: Required. Constant filled by server.
    :type backup_management_type: str
    :param work_load_type: Type of workload for the backup management
    :type work_load_type: str
    :param settings: Common settings for the backup management
    :type settings: ~azure.mgmt.recoveryservicesbackup.models.Settings
    :param sub_protection_policy: List of sub-protection policies which
     includes schedule and retention
    :type sub_protection_policy:
     list[~azure.mgmt.recoveryservicesbackup.models.SubProtectionPolicy]
    """

    _validation = {
        'backup_management_type': {'required': True},
    }

    _attribute_map = {
        'protected_items_count': {'key': 'protectedItemsCount', 'type': 'int'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'work_load_type': {'key': 'workLoadType', 'type': 'str'},
        'settings': {'key': 'settings', 'type': 'Settings'},
        'sub_protection_policy': {'key': 'subProtectionPolicy', 'type': '[SubProtectionPolicy]'},
    }

    def __init__(self, **kwargs):
        super(AzureVmWorkloadProtectionPolicy, self).__init__(**kwargs)
        self.work_load_type = kwargs.get('work_load_type', None)
        self.settings = kwargs.get('settings', None)
        self.sub_protection_policy = kwargs.get('sub_protection_policy', None)
        self.backup_management_type = 'AzureWorkload'
