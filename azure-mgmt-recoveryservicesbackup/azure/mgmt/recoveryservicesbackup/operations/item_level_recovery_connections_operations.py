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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class ItemLevelRecoveryConnectionsOperations(object):
    """ItemLevelRecoveryConnectionsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2016-12-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2016-12-01"

        self.config = config

    def provision(
            self, vault_name, resource_group_name, fabric_name, container_name, protected_item_name, recovery_point_id, parameters, custom_headers=None, raw=False, **operation_config):
        """Provisions a script which invokes an iSCSI connection to the backup
        data. Executing this script opens a file explorer displaying all the
        recoverable files and folders. This is an asynchronous operation. To
        know the status of provisioning, call GetProtectedItemOperationResult
        API.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the
         recovery services vault is present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up
         items.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders
         are to be restored.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up
         data. iSCSI connection will be provisioned for this backed up data.
        :type recovery_point_id: str
        :param parameters: resource ILR request
        :type parameters:
         ~azure.mgmt.recoveryservicesbackup.models.ILRRequestResource
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.provision.metadata['url']
        path_format_arguments = {
            'vaultName': self._serialize.url("vault_name", vault_name, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'fabricName': self._serialize.url("fabric_name", fabric_name, 'str'),
            'containerName': self._serialize.url("container_name", container_name, 'str'),
            'protectedItemName': self._serialize.url("protected_item_name", protected_item_name, 'str'),
            'recoveryPointId': self._serialize.url("recovery_point_id", recovery_point_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ILRRequestResource')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    provision.metadata = {'url': '/Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery'}

    def revoke(
            self, vault_name, resource_group_name, fabric_name, container_name, protected_item_name, recovery_point_id, custom_headers=None, raw=False, **operation_config):
        """Revokes an iSCSI connection which can be used to download a script.
        Executing this script opens a file explorer displaying all recoverable
        files and folders. This is an asynchronous operation.

        :param vault_name: The name of the recovery services vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the
         recovery services vault is present.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up
         items.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders
         are to be restored.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up
         data. iSCSI connection will be revoked for this backed up data.
        :type recovery_point_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.revoke.metadata['url']
        path_format_arguments = {
            'vaultName': self._serialize.url("vault_name", vault_name, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'fabricName': self._serialize.url("fabric_name", fabric_name, 'str'),
            'containerName': self._serialize.url("container_name", container_name, 'str'),
            'protectedItemName': self._serialize.url("protected_item_name", protected_item_name, 'str'),
            'recoveryPointId': self._serialize.url("recovery_point_id", recovery_point_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    revoke.metadata = {'url': '/Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery'}
