"""Adds a network device of one of the following types: ExternalDhcp, ExternalLoadBalancer"""
from baseCmd import *
from baseResponse import *


class addNetworkDeviceCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """parameters for network device"""
        self.networkdeviceparameterlist = []
        self.typeInfo['networkdeviceparameterlist'] = 'map'
        """Network device type, now supports ExternalDhcp, JuniperSRXFirewall, PaloAltoFirewall"""
        self.networkdevicetype = None
        self.typeInfo['networkdevicetype'] = 'string'
        self.required = []


class addNetworkDeviceResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the network device"""
        self.id = None
        self.typeInfo['id'] = 'string'

