"""Deletes network device."""
from baseCmd import *
from baseResponse import *


class deleteNetworkDeviceCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Id of network device to delete"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteNetworkDeviceResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

