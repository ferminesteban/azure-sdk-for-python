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

from .job import Job


class MabJob(Job):
    """MAB workload-specific job.

    All required parameters must be populated in order to send to Azure.

    :param entity_friendly_name: Friendly name of the entity on which the
     current job is executing.
    :type entity_friendly_name: str
    :param backup_management_type: Backup management type to execute the
     current job. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param operation: The operation name.
    :type operation: str
    :param status: Job status.
    :type status: str
    :param start_time: The start time.
    :type start_time: datetime
    :param end_time: The end time.
    :type end_time: datetime
    :param activity_id: ActivityId of job.
    :type activity_id: str
    :param job_type: Required. Constant filled by server.
    :type job_type: str
    :param duration: Time taken by job to run.
    :type duration: timedelta
    :param actions_info: The state/actions applicable on jobs like
     cancel/retry.
    :type actions_info: list[str or
     ~azure.mgmt.recoveryservicesbackup.models.JobSupportedAction]
    :param mab_server_name: Name of server protecting the DS.
    :type mab_server_name: str
    :param mab_server_type: Server type of MAB container. Possible values
     include: 'Invalid', 'Unknown', 'IaasVMContainer',
     'IaasVMServiceContainer', 'DPMContainer', 'AzureBackupServerContainer',
     'MABContainer', 'Cluster', 'AzureSqlContainer', 'Windows', 'VCenter',
     'VMAppContainer', 'SQLAGWorkLoadContainer', 'StorageContainer',
     'GenericContainer'
    :type mab_server_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.MabServerType
    :param workload_type: Workload type of backup item. Possible values
     include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB', 'Exchange',
     'Sharepoint', 'VMwareVM', 'SystemState', 'Client', 'GenericDataSource',
     'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase'
    :type workload_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.WorkloadType
    :param error_details: The errors.
    :type error_details:
     list[~azure.mgmt.recoveryservicesbackup.models.MabErrorInfo]
    :param extended_info: Additional information on the job.
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.MabJobExtendedInfo
    """

    _validation = {
        'job_type': {'required': True},
    }

    _attribute_map = {
        'entity_friendly_name': {'key': 'entityFriendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'duration'},
        'actions_info': {'key': 'actionsInfo', 'type': '[JobSupportedAction]'},
        'mab_server_name': {'key': 'mabServerName', 'type': 'str'},
        'mab_server_type': {'key': 'mabServerType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'error_details': {'key': 'errorDetails', 'type': '[MabErrorInfo]'},
        'extended_info': {'key': 'extendedInfo', 'type': 'MabJobExtendedInfo'},
    }

    def __init__(self, **kwargs):
        super(MabJob, self).__init__(**kwargs)
        self.duration = kwargs.get('duration', None)
        self.actions_info = kwargs.get('actions_info', None)
        self.mab_server_name = kwargs.get('mab_server_name', None)
        self.mab_server_type = kwargs.get('mab_server_type', None)
        self.workload_type = kwargs.get('workload_type', None)
        self.error_details = kwargs.get('error_details', None)
        self.extended_info = kwargs.get('extended_info', None)
        self.job_type = 'MabJob'
