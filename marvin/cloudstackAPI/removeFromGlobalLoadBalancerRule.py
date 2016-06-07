"""Removes a load balancer rule association with global load balancer rule"""
from baseCmd import *
from baseResponse import *


class removeFromGlobalLoadBalancerRuleCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """The ID of the load balancer rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the list load balancer rules that will be assigned to gloabal load balancer rule"""
        """Required"""
        self.loadbalancerrulelist = []
        self.typeInfo['loadbalancerrulelist'] = 'list'
        self.required = ["id", "loadbalancerrulelist", ]


class removeFromGlobalLoadBalancerRuleResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

