"""Returns user data associated with the VM"""
from baseCmd import *
from baseResponse import *


class getVirtualMachineUserDataCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """The ID of the virtual machine"""
        """Required"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        self.required = ["virtualmachineid", ]


class getVirtualMachineUserDataResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """Base 64 encoded VM user data"""
        self.userdata = None
        self.typeInfo['userdata'] = 'string'
        """the ID of the virtual machine"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'string'

