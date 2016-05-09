"""Deletes an traffic monitor host."""
from baseCmd import *
from baseResponse import *


class deleteTrafficMonitorCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Id of the Traffic Monitor Host."""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteTrafficMonitorResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
