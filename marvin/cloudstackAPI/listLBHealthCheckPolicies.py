"""Lists load balancer health check policies."""
from baseCmd import *
from baseResponse import *


class listLBHealthCheckPoliciesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by display flag; only ROOT admin is eligible to pass this parameter"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the ID of the health check policy"""
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


class listLBHealthCheckPoliciesResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the account of the HealthCheck policy"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain of the HealthCheck policy"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the HealthCheck policy"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the LB rule ID"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'string'
        """the id of the zone the HealthCheck policy belongs to"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the list of healthcheckpolicies"""
        self.healthcheckpolicy = []

class healthcheckpolicy:
    def __init__(self):
        """"the LB HealthCheck policy ID"""
        self.id = None
        """"the description of the healthcheck policy"""
        self.description = None
        """"is policy for display to the regular user"""
        self.fordisplay = None
        """"Amount of time between health checks"""
        self.healthcheckinterval = None
        """"Number of consecutive health check success before declaring an instance healthy"""
        self.healthcheckthresshold = None
        """"the pingpath  of the healthcheck policy"""
        self.pingpath = None
        """"Time to wait when receiving a response from the health check"""
        self.responsetime = None
        """"the state of the policy"""
        self.state = None
        """"Number of consecutive health check failures before declaring an instance unhealthy."""
        self.unhealthcheckthresshold = None

