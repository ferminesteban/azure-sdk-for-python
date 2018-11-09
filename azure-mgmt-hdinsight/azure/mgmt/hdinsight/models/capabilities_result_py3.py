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


class CapabilitiesResult(Model):
    """The Get Capabilities operation response.

    :param versions: The version capability.
    :type versions: dict[str, ~azure.mgmt.hdinsight.models.VersionsCapability]
    :param regions: The virtual machine size compatibilty features.
    :type regions: dict[str, ~azure.mgmt.hdinsight.models.RegionsCapability]
    :param vm_sizes: The virtual machine sizes.
    :type vm_sizes: dict[str, ~azure.mgmt.hdinsight.models.VmSizesCapability]
    :param vm_size_filters: The virtual machine size compatibilty filters.
    :type vm_size_filters:
     list[~azure.mgmt.hdinsight.models.VmSizeCompatibilityFilter]
    :param features: The capabilty features.
    :type features: list[str]
    :param quota: The quota capability.
    :type quota: ~azure.mgmt.hdinsight.models.QuotaCapability
    """

    _attribute_map = {
        'versions': {'key': 'versions', 'type': '{VersionsCapability}'},
        'regions': {'key': 'regions', 'type': '{RegionsCapability}'},
        'vm_sizes': {'key': 'vmSizes', 'type': '{VmSizesCapability}'},
        'vm_size_filters': {'key': 'vmSize_filters', 'type': '[VmSizeCompatibilityFilter]'},
        'features': {'key': 'features', 'type': '[str]'},
        'quota': {'key': 'quota', 'type': 'QuotaCapability'},
    }

    def __init__(self, *, versions=None, regions=None, vm_sizes=None, vm_size_filters=None, features=None, quota=None, **kwargs) -> None:
        super(CapabilitiesResult, self).__init__(**kwargs)
        self.versions = versions
        self.regions = regions
        self.vm_sizes = vm_sizes
        self.vm_size_filters = vm_size_filters
        self.features = features
        self.quota = quota
