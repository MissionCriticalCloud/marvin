"""Adds Traffic Monitor Host for Direct Network Usage"""
from baseCmd import *
from baseResponse import *


class addTrafficMonitorCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """URL of the traffic monitor Host"""
        """Required"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """Zone in which to add the external firewall appliance."""
        """Required"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        """Traffic going into the listed zones will not be metered"""
        self.excludezones = None
        self.typeInfo['excludezones'] = 'string'
        """Traffic going into the listed zones will be metered"""
        self.includezones = None
        self.typeInfo['includezones'] = 'string'
        self.required = ["url", "zoneid", ]


class addTrafficMonitorResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the external firewall"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the management IP address of the external firewall"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the number of times to retry requests to the external firewall"""
        self.numretries = None
        self.typeInfo['numretries'] = 'string'
        """the timeout (in seconds) for requests to the external firewall"""
        self.timeout = None
        self.typeInfo['timeout'] = 'string'
        """the zone ID of the external firewall"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
