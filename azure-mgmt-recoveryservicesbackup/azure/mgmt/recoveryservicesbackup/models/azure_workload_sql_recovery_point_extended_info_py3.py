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


class AzureWorkloadSQLRecoveryPointExtendedInfo(Model):
    """Extended info class details.

    :param data_directory_time_in_utc: UTC time at which data directory info
     was captured
    :type data_directory_time_in_utc: datetime
    :param data_directory_paths: List of data directory paths during restore
     operation.
    :type data_directory_paths:
     list[~azure.mgmt.recoveryservicesbackup.models.SQLDataDirectory]
    """

    _attribute_map = {
        'data_directory_time_in_utc': {'key': 'dataDirectoryTimeInUTC', 'type': 'iso-8601'},
        'data_directory_paths': {'key': 'dataDirectoryPaths', 'type': '[SQLDataDirectory]'},
    }

    def __init__(self, *, data_directory_time_in_utc=None, data_directory_paths=None, **kwargs) -> None:
        super(AzureWorkloadSQLRecoveryPointExtendedInfo, self).__init__(**kwargs)
        self.data_directory_time_in_utc = data_directory_time_in_utc
        self.data_directory_paths = data_directory_paths
