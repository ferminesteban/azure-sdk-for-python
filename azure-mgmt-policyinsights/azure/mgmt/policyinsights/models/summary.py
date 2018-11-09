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


class Summary(Model):
    """Summary results.

    :param odataid: OData entity ID; always set to null since summaries do not
     have an entity ID.
    :type odataid: str
    :param odatacontext: OData context string; used by OData clients to
     resolve type information based on metadata.
    :type odatacontext: str
    :param results: Non-compliance summary for all policy assignments.
    :type results: ~azure.mgmt.policyinsights.models.SummaryResults
    :param policy_assignments: Policy assignments summary.
    :type policy_assignments:
     list[~azure.mgmt.policyinsights.models.PolicyAssignmentSummary]
    """

    _attribute_map = {
        'odataid': {'key': '@odata\\.id', 'type': 'str'},
        'odatacontext': {'key': '@odata\\.context', 'type': 'str'},
        'results': {'key': 'results', 'type': 'SummaryResults'},
        'policy_assignments': {'key': 'policyAssignments', 'type': '[PolicyAssignmentSummary]'},
    }

    def __init__(self, **kwargs):
        super(Summary, self).__init__(**kwargs)
        self.odataid = kwargs.get('odataid', None)
        self.odatacontext = kwargs.get('odatacontext', None)
        self.results = kwargs.get('results', None)
        self.policy_assignments = kwargs.get('policy_assignments', None)
