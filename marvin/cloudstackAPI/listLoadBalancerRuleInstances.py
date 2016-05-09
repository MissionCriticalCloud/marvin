"""List all virtual machine instances that are assigned to a load balancer rule."""
from baseCmd import *
from baseResponse import *


class listLoadBalancerRuleInstancesCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the ID of the load balancer rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """true if listing all virtual machines currently applied to the load balancer rule; default is true"""
        self.applied = None
        self.typeInfo['applied'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """true if load balancer rule VM IP information to be included; default is false"""
        self.lbvmips = None
        self.typeInfo['lbvmips'] = 'boolean'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = ["id", ]


class listLoadBalancerRuleInstancesResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """IP addresses of the vm set of lb rule"""
        self.lbvmipaddresses = None
        self.typeInfo['lbvmipaddresses'] = 'list'
        """the user vm set for lb rule"""
        self.loadbalancerruleinstance = None
        self.typeInfo['loadbalancerruleinstance'] = 'uservmresponse'
