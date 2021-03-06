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


class DirectLineSite(Model):
    """A site for the Direct Line channel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar site_id: Site Id
    :vartype site_id: str
    :param site_name: Required. Site name
    :type site_name: str
    :ivar key: Primary key. Value only returned through POST to the action
     Channel List API, otherwise empty.
    :vartype key: str
    :ivar key2: Secondary key. Value only returned through POST to the action
     Channel List API, otherwise empty.
    :vartype key2: str
    :param is_enabled: Required. Whether this site is enabled for DirectLine
     channel
    :type is_enabled: bool
    :param is_v1_enabled: Required. Whether this site is enabled for Bot
     Framework V1 protocol
    :type is_v1_enabled: bool
    :param is_v3_enabled: Required. Whether this site is enabled for Bot
     Framework V1 protocol
    :type is_v3_enabled: bool
    """

    _validation = {
        'site_id': {'readonly': True},
        'site_name': {'required': True},
        'key': {'readonly': True},
        'key2': {'readonly': True},
        'is_enabled': {'required': True},
        'is_v1_enabled': {'required': True},
        'is_v3_enabled': {'required': True},
    }

    _attribute_map = {
        'site_id': {'key': 'siteId', 'type': 'str'},
        'site_name': {'key': 'siteName', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'key2': {'key': 'key2', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_v1_enabled': {'key': 'isV1Enabled', 'type': 'bool'},
        'is_v3_enabled': {'key': 'isV3Enabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DirectLineSite, self).__init__(**kwargs)
        self.site_id = None
        self.site_name = kwargs.get('site_name', None)
        self.key = None
        self.key2 = None
        self.is_enabled = kwargs.get('is_enabled', None)
        self.is_v1_enabled = kwargs.get('is_v1_enabled', None)
        self.is_v3_enabled = kwargs.get('is_v3_enabled', None)
