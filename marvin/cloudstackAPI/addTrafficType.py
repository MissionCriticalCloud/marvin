"""Adds traffic type to a physical network"""
from baseCmd import *
from baseResponse import *


class addTrafficTypeCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the Physical Network ID"""
        """Required"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'uuid'
        """the trafficType to be added to the physical network"""
        """Required"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        """Used if physical network has multiple isolation types and traffic type is public. Choose which isolation method. Valid options currently 'vlan' or 'vxlan', defaults to 'vlan'."""
        self.isolationmethod = None
        self.typeInfo['isolationmethod'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        self.typeInfo['kvmnetworklabel'] = 'string'
        """The network name of the physical device dedicated to this traffic on an OVM3 host"""
        self.ovm3networklabel = None
        self.typeInfo['ovm3networklabel'] = 'string'
        """The VLAN id to be used for Management traffic by the host"""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None
        self.typeInfo['xennetworklabel'] = 'string'
        self.required = ["physicalnetworkid", "traffictype", ]


class addTrafficTypeResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """id of the network provider"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        self.typeInfo['kvmnetworklabel'] = 'string'
        """The network name of the physical device dedicated to this traffic on an OVM3 host"""
        self.ovm3networklabel = None
        self.typeInfo['ovm3networklabel'] = 'string'
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """the trafficType to be added to the physical network"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None
        self.typeInfo['xennetworklabel'] = 'string'

