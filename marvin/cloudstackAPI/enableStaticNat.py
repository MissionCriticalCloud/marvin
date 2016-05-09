"""Enables static NAT for given IP address"""
from baseCmd import *
from baseResponse import *
class enableStaticNatCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the public IP address ID for which static NAT feature is being enabled"""
        """Required"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'uuid'
        """the ID of the virtual machine for enabling static NAT feature"""
        """Required"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        """The network of the VM the static NAT will be enabled for. Required when public IP address is not associated with any guest network yet (VPC case)"""
        self.networkid = None
        self.typeInfo['networkid'] = 'uuid'
        """VM guest NIC secondary IP address for the port forwarding rule"""
        self.vmguestip = None
        self.typeInfo['vmguestip'] = 'string'
        self.required = ["ipaddressid","virtualmachineid",]

class enableStaticNatResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

