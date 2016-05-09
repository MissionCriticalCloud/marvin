"""Updates load balancer stickiness policy"""
from baseCmd import *
from baseResponse import *


class updateLBStickinessPolicyCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """id of lb stickiness policy"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the policy to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["id", ]


class updateLBStickinessPolicyResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the account of the Stickiness policy"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the description of the Stickiness policy"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the domain of the Stickiness policy"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the Stickiness policy"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the LB rule ID"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'string'
        """the name of the Stickiness policy"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the state of the policy"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the id of the zone the Stickiness policy belongs to"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the list of stickinesspolicies"""
        self.stickinesspolicy = []


class stickinesspolicy:
    def __init__(self):
        """"the LB Stickiness policy ID"""
        self.id = None
        """"the description of the Stickiness policy"""
        self.description = None
        """"is policy for display to the regular user"""
        self.fordisplay = None
        """"the method name of the Stickiness policy"""
        self.methodname = None
        """"the name of the Stickiness policy"""
        self.name = None
        """"the params of the policy"""
        self.params = None
        """"the state of the policy"""
        self.state = None
