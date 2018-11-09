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


class EntityId(Model):
    """A Data Lake Analytics catalog entity identifier object.

    :param name: the name of the external table associated with this database,
     schema and table.
    :type name: ~azure.mgmt.datalake.analytics.catalog.models.DdlName
    :param version: the version of the external data source.
    :type version: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'DdlName'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EntityId, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.version = kwargs.get('version', None)
