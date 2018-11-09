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


class DefaultKey(Model):
    """Class to specify properties of default content key for each encryption
    scheme.

    :param label: Label can be used to specify Content Key when creating a
     Streaming Locator
    :type label: str
    :param policy_name: Policy used by Default Key
    :type policy_name: str
    """

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DefaultKey, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self.policy_name = kwargs.get('policy_name', None)
