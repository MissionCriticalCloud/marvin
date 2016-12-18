"""Updates traffic type of a physical network"""
from baseCmd import *
from baseResponse import *


class updateTrafficTypeCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """traffic type id"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        self.typeInfo['kvmnetworklabel'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None
        self.typeInfo['xennetworklabel'] = 'string'
        self.required = ["id", ]


class updateTrafficTypeResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """id of the network provider"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        self.typeInfo['kvmnetworklabel'] = 'string'
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """the trafficType to be added to the physical network"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None
        self.typeInfo['xennetworklabel'] = 'string'

