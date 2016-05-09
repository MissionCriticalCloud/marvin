"""Updates the information about Guest OS to Hypervisor specific name mapping"""
from baseCmd import *
from baseResponse import *


class updateGuestOsMappingCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """UUID of the Guest OS to hypervisor name Mapping"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Hypervisor specific name for this Guest OS"""
        """Required"""
        self.osnameforhypervisor = None
        self.typeInfo['osnameforhypervisor'] = 'string'
        self.required = ["id", "osnameforhypervisor", ]


class updateGuestOsMappingResponse(baseResponse):
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
