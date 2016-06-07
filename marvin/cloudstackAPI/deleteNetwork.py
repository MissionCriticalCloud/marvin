"""Deletes a network"""
from baseCmd import *
from baseResponse import *


class deleteNetworkCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the network"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Force delete a network. Network will be marked as 'Destroy' even when commands to shutdown and cleanup to the backend fails."""
        self.forced = None
        self.typeInfo['forced'] = 'boolean'
        self.required = ["id", ]


class deleteNetworkResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

