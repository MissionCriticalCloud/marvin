"""Deletes a user for an account"""
from baseCmd import *
from baseResponse import *


class deleteUserCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """id of the user to be deleted"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteUserResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
