"""Adds a guest OS name to hypervisor OS name mapping"""
from baseCmd import *
from baseResponse import *
class addGuestOsMappingCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """Hypervisor type. One of : XenServer, KVM"""
        """Required"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """Hypervisor version to create the mapping for. Use 'default' for default versions"""
        """Required"""
        self.hypervisorversion = None
        self.typeInfo['hypervisorversion'] = 'string'
        """OS name specific to the hypervisor"""
        """Required"""
        self.osnameforhypervisor = None
        self.typeInfo['osnameforhypervisor'] = 'string'
        """Display Name of Guest OS standard type. Either Display Name or UUID must be passed"""
        self.osdisplayname = None
        self.typeInfo['osdisplayname'] = 'string'
        """UUID of Guest OS type. Either the UUID or Display Name must be passed"""
        self.ostypeid = None
        self.typeInfo['ostypeid'] = 'uuid'
        self.required = ["hypervisor","hypervisorversion","osnameforhypervisor",]

class addGuestOsMappingResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the Guest OS mapping"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the hypervisor"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """version of the hypervisor for mapping"""
        self.hypervisorversion = None
        self.typeInfo['hypervisorversion'] = 'string'
        """is the mapping user defined"""
        self.isuserdefined = None
        self.typeInfo['isuserdefined'] = 'string'
        """standard display name for the Guest OS"""
        self.osdisplayname = None
        self.typeInfo['osdisplayname'] = 'string'
        """hypervisor specific name for the Guest OS"""
        self.osnameforhypervisor = None
        self.typeInfo['osnameforhypervisor'] = 'string'
        """the ID of the Guest OS type"""
        self.ostypeid = None
        self.typeInfo['ostypeid'] = 'string'

