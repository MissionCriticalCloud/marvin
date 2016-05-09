"""Updates an existing autoscale policy."""
from baseCmd import *
from baseResponse import *


class updateAutoScalePolicyCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale policy"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the list of IDs of the conditions that are being evaluated on every interval"""
        self.conditionids = []
        self.typeInfo['conditionids'] = 'list'
        """the duration for which the conditions have to be true before action is taken"""
        self.duration = None
        self.typeInfo['duration'] = 'integer'
        """the cool down period for which the policy should not be evaluated after the action has been taken"""
        self.quiettime = None
        self.typeInfo['quiettime'] = 'integer'
        self.required = ["id", ]


class updateAutoScalePolicyResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the autoscale policy ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the autoscale policy"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the action to be executed if all the conditions evaluate to true for the specified duration."""
        self.action = None
        self.typeInfo['action'] = 'string'
        """the list of IDs of the conditions that are being evaluated on every interval"""
        self.conditions = None
        self.typeInfo['conditions'] = 'list'
        """the domain name of the autoscale policy"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the autoscale policy"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the duration for which the conditions have to be true before action is taken"""
        self.duration = None
        self.typeInfo['duration'] = 'integer'
        """the project name of the autoscale policy"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id autoscale policy"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the cool down period for which the policy should not be evaluated after the action has been taken"""
        self.quiettime = None
        self.typeInfo['quiettime'] = 'integer'
