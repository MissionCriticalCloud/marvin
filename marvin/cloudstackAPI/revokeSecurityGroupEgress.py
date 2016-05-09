"""Deletes a particular egress rule from this security group"""
from baseCmd import *
from baseResponse import *
class revokeSecurityGroupEgressCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """The ID of the egress rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id",]

class revokeSecurityGroupEgressResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

