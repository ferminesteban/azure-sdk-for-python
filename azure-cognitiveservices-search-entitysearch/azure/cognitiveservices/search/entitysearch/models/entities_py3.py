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

from .search_results_answer import SearchResultsAnswer


class Entities(SearchResultsAnswer):
    """Defines an entity answer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar contractual_rules: A list of rules that you must adhere to if you
     display the item.
    :vartype contractual_rules:
     list[~azure.cognitiveservices.search.entitysearch.models.ContractualRulesContractualRule]
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar query_context:
    :vartype query_context:
     ~azure.cognitiveservices.search.entitysearch.models.QueryContext
    :ivar query_scenario: The supported query scenario. This field is set to
     DominantEntity or DisambiguationItem. The field is set to DominantEntity
     if Bing determines that only a single entity satisfies the request. For
     example, a book, movie, person, or attraction. If multiple entities could
     satisfy the request, the field is set to DisambiguationItem. For example,
     if the request uses the generic title of a movie franchise, the entity's
     type would likely be DisambiguationItem. But, if the request specifies a
     specific title from the franchise, the entity's type would likely be
     DominantEntity. Possible values include: 'DominantEntity',
     'DominantEntityWithDisambiguation', 'Disambiguation', 'List',
     'ListWithPivot'. Default value: "DominantEntity" .
    :vartype query_scenario: str or
     ~azure.cognitiveservices.search.entitysearch.models.EntityQueryScenario
    :param value: Required. A list of entities.
    :type value:
     list[~azure.cognitiveservices.search.entitysearch.models.Thing]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'contractual_rules': {'readonly': True},
        'web_search_url': {'readonly': True},
        'query_context': {'readonly': True},
        'query_scenario': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'contractual_rules': {'key': 'contractualRules', 'type': '[ContractualRulesContractualRule]'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'query_scenario': {'key': 'queryScenario', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Thing]'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(Entities, self).__init__(**kwargs)
        self.query_scenario = None
        self.value = value
        self._type = 'Entities'
