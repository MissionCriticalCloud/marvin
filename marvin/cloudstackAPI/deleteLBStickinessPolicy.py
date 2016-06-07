"""Deletes a load balancer stickiness policy."""
from baseCmd import *
from baseResponse import *


class deleteLBStickinessPolicyCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the LB stickiness policy"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteLBStickinessPolicyResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

