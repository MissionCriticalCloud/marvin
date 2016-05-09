"""Updates load balancer health check policy"""
from baseCmd import *
from baseResponse import *
class updateLBHealthCheckPolicyCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """ID of load balancer health check policy"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the policy to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["id",]

class updateLBHealthCheckPolicyResponse (baseResponse):
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

