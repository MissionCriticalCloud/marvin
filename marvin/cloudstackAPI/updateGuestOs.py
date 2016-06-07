"""Updates the information about Guest OS"""
from baseCmd import *
from baseResponse import *


class updateGuestOsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """UUID of the Guest OS"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Unique display name for Guest OS"""
        """Required"""
        self.osdisplayname = None
        self.typeInfo['osdisplayname'] = 'string'
        self.required = ["id", "osdisplayname", ]


class updateGuestOsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the OS type"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the name/description of the OS type"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """is the guest OS user defined"""
        self.isuserdefined = None
        self.typeInfo['isuserdefined'] = 'string'
        """the ID of the OS category"""
        self.oscategoryid = None
        self.typeInfo['oscategoryid'] = 'string'

