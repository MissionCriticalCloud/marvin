"""Adds account to a project"""
from baseCmd import *
from baseResponse import *


class addAccountToProjectCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """ID of the project to add the account to"""
        """Required"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """name of the account to be added to the project"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """email to which invitation to the project is going to be sent"""
        self.email = None
        self.typeInfo['email'] = 'string'
        self.required = ["projectid", ]


class addAccountToProjectResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

