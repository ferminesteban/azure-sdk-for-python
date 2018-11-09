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


class Hair(Model):
    """Properties describing hair attributes.

    :param bald: A number describing confidence level of whether the person is
     bald.
    :type bald: float
    :param invisible: A boolean value describing whether the hair is visible
     in the image.
    :type invisible: bool
    :param hair_color: An array of candidate colors and confidence level in
     the presence of each.
    :type hair_color:
     list[~azure.cognitiveservices.vision.face.models.HairColor]
    """

    _attribute_map = {
        'bald': {'key': 'bald', 'type': 'float'},
        'invisible': {'key': 'invisible', 'type': 'bool'},
        'hair_color': {'key': 'hairColor', 'type': '[HairColor]'},
    }

    def __init__(self, *, bald: float=None, invisible: bool=None, hair_color=None, **kwargs) -> None:
        super(Hair, self).__init__(**kwargs)
        self.bald = bald
        self.invisible = invisible
        self.hair_color = hair_color
