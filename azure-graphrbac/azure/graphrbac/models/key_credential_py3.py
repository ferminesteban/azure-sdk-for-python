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


class KeyCredential(Model):
    """Active Directory Key Credential information.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param start_date: Start date.
    :type start_date: datetime
    :param end_date: End date.
    :type end_date: datetime
    :param value: Key value.
    :type value: str
    :param key_id: Key ID.
    :type key_id: str
    :param usage: Usage. Acceptable values are 'Verify' and 'Sign'.
    :type usage: str
    :param type: Type. Acceptable values are 'AsymmetricX509Cert' and
     'Symmetric'.
    :type type: str
    :param custom_key_identifier: Custom Key Identifier
    :type custom_key_identifier: bytearray
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'str'},
        'key_id': {'key': 'keyId', 'type': 'str'},
        'usage': {'key': 'usage', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'custom_key_identifier': {'key': 'customKeyIdentifier', 'type': 'bytearray'},
    }

    def __init__(self, *, additional_properties=None, start_date=None, end_date=None, value: str=None, key_id: str=None, usage: str=None, type: str=None, custom_key_identifier: bytearray=None, **kwargs) -> None:
        super(KeyCredential, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.start_date = start_date
        self.end_date = end_date
        self.value = value
        self.key_id = key_id
        self.usage = usage
        self.type = type
        self.custom_key_identifier = custom_key_identifier
