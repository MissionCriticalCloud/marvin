"""Creates a load balancer health check policy"""
from baseCmd import *
from baseResponse import *


class createLBHealthCheckPolicyCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the load balancer rule"""
        """Required"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'uuid'
        """the description of the load balancer health check policy"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """an optional field, whether to the display the rule to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """Number of consecutive health check success before declaring an instance healthy"""
        self.healthythreshold = None
        self.typeInfo['healthythreshold'] = 'integer'
        """Amount of time between health checks (1 sec - 20940 sec)"""
        self.intervaltime = None
        self.typeInfo['intervaltime'] = 'integer'
        """HTTP ping path"""
        self.pingpath = None
        self.typeInfo['pingpath'] = 'string'
        """Time to wait when receiving a response from the health check (2sec - 60 sec)"""
        self.responsetimeout = None
        self.typeInfo['responsetimeout'] = 'integer'
        """Number of consecutive health check failures before declaring an instance unhealthy"""
        self.unhealthythreshold = None
        self.typeInfo['unhealthythreshold'] = 'integer'
        self.required = ["lbruleid", ]


class createLBHealthCheckPolicyResponse (baseResponse):
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

