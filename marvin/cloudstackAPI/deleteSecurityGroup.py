"""Deletes security group"""
from baseCmd import *
from baseResponse import *


class deleteSecurityGroupCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the account of the security group. Must be specified with domain ID"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain ID of account owning the security group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """The ID of the security group. Mutually exclusive with name parameter"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """The ID of the security group. Mutually exclusive with id parameter"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project of the security group"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = []


class deleteSecurityGroupResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

