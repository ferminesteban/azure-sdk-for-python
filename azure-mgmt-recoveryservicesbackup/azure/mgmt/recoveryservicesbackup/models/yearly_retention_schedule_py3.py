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


class YearlyRetentionSchedule(Model):
    """Yearly retention schedule.

    :param retention_schedule_format_type: Retention schedule format for
     yearly retention policy. Possible values include: 'Invalid', 'Daily',
     'Weekly'
    :type retention_schedule_format_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RetentionScheduleFormat
    :param months_of_year: List of months of year of yearly retention policy.
    :type months_of_year: list[str or
     ~azure.mgmt.recoveryservicesbackup.models.MonthOfYear]
    :param retention_schedule_daily: Daily retention format for yearly
     retention policy.
    :type retention_schedule_daily:
     ~azure.mgmt.recoveryservicesbackup.models.DailyRetentionFormat
    :param retention_schedule_weekly: Weekly retention format for yearly
     retention policy.
    :type retention_schedule_weekly:
     ~azure.mgmt.recoveryservicesbackup.models.WeeklyRetentionFormat
    :param retention_times: Retention times of retention policy.
    :type retention_times: list[datetime]
    :param retention_duration: Retention duration of retention Policy.
    :type retention_duration:
     ~azure.mgmt.recoveryservicesbackup.models.RetentionDuration
    """

    _attribute_map = {
        'retention_schedule_format_type': {'key': 'retentionScheduleFormatType', 'type': 'str'},
        'months_of_year': {'key': 'monthsOfYear', 'type': '[MonthOfYear]'},
        'retention_schedule_daily': {'key': 'retentionScheduleDaily', 'type': 'DailyRetentionFormat'},
        'retention_schedule_weekly': {'key': 'retentionScheduleWeekly', 'type': 'WeeklyRetentionFormat'},
        'retention_times': {'key': 'retentionTimes', 'type': '[iso-8601]'},
        'retention_duration': {'key': 'retentionDuration', 'type': 'RetentionDuration'},
    }

    def __init__(self, *, retention_schedule_format_type=None, months_of_year=None, retention_schedule_daily=None, retention_schedule_weekly=None, retention_times=None, retention_duration=None, **kwargs) -> None:
        super(YearlyRetentionSchedule, self).__init__(**kwargs)
        self.retention_schedule_format_type = retention_schedule_format_type
        self.months_of_year = months_of_year
        self.retention_schedule_daily = retention_schedule_daily
        self.retention_schedule_weekly = retention_schedule_weekly
        self.retention_times = retention_times
        self.retention_duration = retention_duration
