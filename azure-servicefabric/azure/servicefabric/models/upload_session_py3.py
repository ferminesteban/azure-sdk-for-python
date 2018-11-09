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


class UploadSession(Model):
    """Information about a image store upload session.

    :param upload_sessions: When querying upload session by upload session ID,
     the result contains only one upload session. When querying upload session
     by image store relative path, the result might contain multiple upload
     sessions.
    :type upload_sessions: list[~azure.servicefabric.models.UploadSessionInfo]
    """

    _attribute_map = {
        'upload_sessions': {'key': 'UploadSessions', 'type': '[UploadSessionInfo]'},
    }

    def __init__(self, *, upload_sessions=None, **kwargs) -> None:
        super(UploadSession, self).__init__(**kwargs)
        self.upload_sessions = upload_sessions
