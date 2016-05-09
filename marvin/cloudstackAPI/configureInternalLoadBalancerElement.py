"""Configures an Internal Load Balancer element."""
from baseCmd import *
from baseResponse import *
class configureInternalLoadBalancerElementCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """the ID of the internal lb provider"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Enables/Disables the Internal Load Balancer element"""
        """Required"""
        self.enabled = None
        self.typeInfo['enabled'] = 'boolean'
        self.required = ["id","enabled",]

class configureInternalLoadBalancerElementResponse (baseResponse):
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

