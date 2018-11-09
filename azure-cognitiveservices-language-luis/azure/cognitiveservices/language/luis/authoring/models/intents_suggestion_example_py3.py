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


class IntentsSuggestionExample(Model):
    """Predicted/suggested intent.

    :param text: The utterance. E.g.: what's the weather like in seattle?
    :type text: str
    :param tokenized_text: The utterance tokenized.
    :type tokenized_text: list[str]
    :param intent_predictions: Predicted/suggested intents.
    :type intent_predictions:
     list[~azure.cognitiveservices.language.luis.authoring.models.IntentPrediction]
    :param entity_predictions: Predicted/suggested entities.
    :type entity_predictions:
     list[~azure.cognitiveservices.language.luis.authoring.models.EntityPrediction]
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'tokenized_text': {'key': 'tokenizedText', 'type': '[str]'},
        'intent_predictions': {'key': 'intentPredictions', 'type': '[IntentPrediction]'},
        'entity_predictions': {'key': 'entityPredictions', 'type': '[EntityPrediction]'},
    }

    def __init__(self, *, text: str=None, tokenized_text=None, intent_predictions=None, entity_predictions=None, **kwargs) -> None:
        super(IntentsSuggestionExample, self).__init__(**kwargs)
        self.text = text
        self.tokenized_text = tokenized_text
        self.intent_predictions = intent_predictions
        self.entity_predictions = entity_predictions
