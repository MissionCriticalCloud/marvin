"""Assigns a certificate to a load balancer rule"""
from baseCmd import *
from baseResponse import *


class assignCertToLoadBalancerCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the certificate"""
        """Required"""
        self.certid = None
        self.typeInfo['certid'] = 'uuid'
        """the ID of the load balancer rule"""
        """Required"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'uuid'
        self.required = ["certid", "lbruleid", ]


class assignCertToLoadBalancerResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
