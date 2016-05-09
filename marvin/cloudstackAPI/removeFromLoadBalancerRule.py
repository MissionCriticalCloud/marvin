"""Removes a virtual machine or a list of virtual machines from a load balancer rule."""
from baseCmd import *
from baseResponse import *
class removeFromLoadBalancerRuleCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """The ID of the load balancer rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the list of IDs of the virtual machines that are being removed from the load balancer rule (i.e. virtualMachineIds=1,2,3)"""
        self.virtualmachineids = []
        self.typeInfo['virtualmachineids'] = 'list'
        """VM ID and IP map, vmidipmap[0].vmid=1 vmidipmap[0].ip=10.1.1.75"""
        self.vmidipmap = []
        self.typeInfo['vmidipmap'] = 'map'
        self.required = ["id",]

class removeFromLoadBalancerRuleResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

