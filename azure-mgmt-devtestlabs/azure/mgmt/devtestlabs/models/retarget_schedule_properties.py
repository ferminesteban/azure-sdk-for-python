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


class RetargetScheduleProperties(Model):
    """Properties for retargeting a virtual machine schedule.

    :param current_resource_id: The resource Id of the virtual machine on
     which the schedule operates
    :type current_resource_id: str
    :param target_resource_id: The resource Id of the virtual machine that the
     schedule should be retargeted to
    :type target_resource_id: str
    """

    _attribute_map = {
        'current_resource_id': {'key': 'currentResourceId', 'type': 'str'},
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
    }

    def __init__(self, current_resource_id=None, target_resource_id=None):
        super(RetargetScheduleProperties, self).__init__()
        self.current_resource_id = current_resource_id
        self.target_resource_id = target_resource_id
