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

from msrest.serialization import Model


class StorageProfile(Model):
    """The storage profile.

    :param storageaccounts: The list of storage accounts in the cluster.
    :type storageaccounts: list[~azure.mgmt.hdinsight.models.StorageAccount]
    """

    _attribute_map = {
        'storageaccounts': {'key': 'storageaccounts', 'type': '[StorageAccount]'},
    }

    def __init__(self, **kwargs):
        super(StorageProfile, self).__init__(**kwargs)
        self.storageaccounts = kwargs.get('storageaccounts', None)
