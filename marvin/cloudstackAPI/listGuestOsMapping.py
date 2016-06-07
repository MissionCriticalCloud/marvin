"""Lists all available OS mappings for given hypervisor"""
from baseCmd import *
from baseResponse import *


class listGuestOsMappingCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list Guest OS mapping by hypervisor"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """list Guest OS mapping by hypervisor version. Must be used with hypervisor parameter"""
        self.hypervisorversion = None
        self.typeInfo['hypervisorversion'] = 'string'
        """list mapping by its UUID"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """list mapping by Guest OS Type UUID"""
        self.ostypeid = None
        self.typeInfo['ostypeid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listGuestOsMappingResponse (baseResponse):
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

