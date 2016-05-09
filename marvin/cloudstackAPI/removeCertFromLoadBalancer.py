"""Removes a certificate from a load balancer rule"""
from baseCmd import *
from baseResponse import *
class removeCertFromLoadBalancerCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """the ID of the load balancer rule"""
        """Required"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'uuid'
        self.required = ["lbruleid",]

class removeCertFromLoadBalancerResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

