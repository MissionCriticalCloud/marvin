"""Add a new guest OS type"""
from baseCmd import *
from baseResponse import *


class addGuestOsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """ID of Guest OS category"""
        """Required"""
        self.oscategoryid = None
        self.typeInfo['oscategoryid'] = 'uuid'
        """Unique display name for Guest OS"""
        """Required"""
        self.osdisplayname = None
        self.typeInfo['osdisplayname'] = 'string'
        """Optional name for Guest OS"""
        self.name = None
        self.typeInfo['name'] = 'string'
        self.required = ["oscategoryid", "osdisplayname", ]


class addGuestOsResponse(baseResponse):
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
