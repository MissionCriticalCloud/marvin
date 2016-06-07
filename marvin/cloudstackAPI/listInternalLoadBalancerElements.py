"""Lists all available Internal Load Balancer elements."""
from baseCmd import *
from baseResponse import *


class listInternalLoadBalancerElementsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list internal load balancer elements by enabled state"""
        self.enabled = None
        self.typeInfo['enabled'] = 'boolean'
        """list internal load balancer elements by id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """list internal load balancer elements by network service provider id"""
        self.nspid = None
        self.typeInfo['nspid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listInternalLoadBalancerElementsResponse (baseResponse):
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

