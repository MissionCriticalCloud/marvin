"""Lists load balancer stickiness policies."""
from baseCmd import *
from baseResponse import *


class listLBStickinessPoliciesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by display flag; only ROOT admin is eligible to pass this parameter"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the ID of the load balancer stickiness policy"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """the ID of the load balancer rule"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listLBStickinessPoliciesResponse (baseResponse):
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

