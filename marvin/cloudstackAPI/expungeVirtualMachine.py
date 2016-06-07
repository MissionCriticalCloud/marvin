"""Expunge a virtual machine. Once expunged, it cannot be recoverd."""
from baseCmd import *
from baseResponse import *


class expungeVirtualMachineCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """The ID of the virtual machine"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class expungeVirtualMachineResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

