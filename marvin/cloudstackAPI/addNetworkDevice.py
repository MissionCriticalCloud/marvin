"""Adds a network device of one of the following types: ExternalDhcp, ExternalFirewall, ExternalLoadBalancer, PxeServer"""
from baseCmd import *
from baseResponse import *


class addNetworkDeviceCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """parameters for network device"""
        self.networkdeviceparameterlist = []
        self.typeInfo['networkdeviceparameterlist'] = 'map'
        """Network device type, now supports ExternalDhcp, PxeServer, JuniperSRXFirewall, PaloAltoFirewall"""
        self.networkdevicetype = None
        self.typeInfo['networkdevicetype'] = 'string'
        self.required = []


class addNetworkDeviceResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the network device"""
        self.id = None
        self.typeInfo['id'] = 'string'

