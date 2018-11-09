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


class RecognizedEntityGroup(Model):
    """Defines a group of previously recognized entities.

    All required parameters must be populated in order to send to Azure.

    :param recognized_entity_regions: Required. The regions of the image that
     contain entities.
    :type recognized_entity_regions:
     list[~azure.cognitiveservices.search.imagesearch.models.RecognizedEntityRegion]
    :param name: Required. The name of the group where images of the entity
     were also found. The following are possible groups.
     CelebRecognitionAnnotations: Similar to CelebrityAnnotations but provides
     a higher probability of an accurate match. CelebrityAnnotations: Contains
     celebrities such as actors, politicians, athletes, and historical figures.
    :type name: str
    """

    _validation = {
        'recognized_entity_regions': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'recognized_entity_regions': {'key': 'recognizedEntityRegions', 'type': '[RecognizedEntityRegion]'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RecognizedEntityGroup, self).__init__(**kwargs)
        self.recognized_entity_regions = kwargs.get('recognized_entity_regions', None)
        self.name = kwargs.get('name', None)
