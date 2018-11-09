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


class TestRouteInput(Model):
    """Input for testing route.

    All required parameters must be populated in order to send to Azure.

    :param message: Routing message
    :type message: ~azure.mgmt.iothub.models.RoutingMessage
    :param route: Required. Route properties
    :type route: ~azure.mgmt.iothub.models.RouteProperties
    """

    _validation = {
        'route': {'required': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'RoutingMessage'},
        'route': {'key': 'route', 'type': 'RouteProperties'},
    }

    def __init__(self, *, route, message=None, **kwargs) -> None:
        super(TestRouteInput, self).__init__(**kwargs)
        self.message = message
        self.route = route
