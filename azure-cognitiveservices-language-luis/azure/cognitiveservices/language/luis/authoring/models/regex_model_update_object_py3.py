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


class RegexModelUpdateObject(Model):
    """Model object for updating a regex entity model.

    :param regex_pattern: The regex entity pattern.
    :type regex_pattern: str
    :param name: The model name.
    :type name: str
    """

    _attribute_map = {
        'regex_pattern': {'key': 'regexPattern', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, regex_pattern: str=None, name: str=None, **kwargs) -> None:
        super(RegexModelUpdateObject, self).__init__(**kwargs)
        self.regex_pattern = regex_pattern
        self.name = name
