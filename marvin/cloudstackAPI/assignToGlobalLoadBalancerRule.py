"""Assign load balancer rule or list of load balancer rules to a global load balancer rules."""
from baseCmd import *
from baseResponse import *
class assignToGlobalLoadBalancerRuleCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """the ID of the global load balancer rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the list load balancer rules that will be assigned to global load balancer rule"""
        """Required"""
        self.loadbalancerrulelist = []
        self.typeInfo['loadbalancerrulelist'] = 'list'
        """Map of LB rule id's and corresponding weights (between 1-100) in the GSLB rule, if not specified weight of a LB rule is defaulted to 1. Specified as 'gslblbruleweightsmap[0].loadbalancerid=UUID&gslblbruleweightsmap[0].weight=10'"""
        self.gslblbruleweightsmap = []
        self.typeInfo['gslblbruleweightsmap'] = 'map'
        self.required = ["id","loadbalancerrulelist",]

class assignToGlobalLoadBalancerRuleResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

