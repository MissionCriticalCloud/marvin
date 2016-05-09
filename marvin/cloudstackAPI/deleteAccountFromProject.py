"""Deletes account from the project"""
from baseCmd import *
from baseResponse import *


class deleteAccountFromProjectCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """name of the account to be removed from the project"""
        """Required"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """ID of the project to remove the account from"""
        """Required"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["account", "projectid", ]


class deleteAccountFromProjectResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
