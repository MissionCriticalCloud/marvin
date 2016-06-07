"""Deletes traffic type of a physical network"""
from baseCmd import *
from baseResponse import *


class deleteTrafficTypeCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """traffic type id"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteTrafficTypeResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

