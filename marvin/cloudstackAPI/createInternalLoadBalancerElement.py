"""Create an Internal Load Balancer element."""
from baseCmd import *
from baseResponse import *


class createInternalLoadBalancerElementCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the network service provider ID of the internal load balancer element"""
        """Required"""
        self.nspid = None
        self.typeInfo['nspid'] = 'uuid'
        self.required = ["nspid", ]


class createInternalLoadBalancerElementResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the internal load balancer element"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Enabled/Disabled the element"""
        self.enabled = None
        self.typeInfo['enabled'] = 'boolean'
        """the physical network service provider id of the element"""
        self.nspid = None
        self.typeInfo['nspid'] = 'string'
