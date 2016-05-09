"""Deletes affinity group"""
from baseCmd import *
from baseResponse import *


class deleteAffinityGroupCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the account of the affinity group. Must be specified with domain ID"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain ID of account owning the affinity group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """The ID of the affinity group. Mutually exclusive with name parameter"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """The name of the affinity group. Mutually exclusive with ID parameter"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project of the affinity group"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = []


class deleteAffinityGroupResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
