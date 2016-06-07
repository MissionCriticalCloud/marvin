"""Deletes a vmsnapshot."""
from baseCmd import *
from baseResponse import *


class deleteVMSnapshotCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """The ID of the VM snapshot"""
        """Required"""
        self.vmsnapshotid = None
        self.typeInfo['vmsnapshotid'] = 'uuid'
        self.required = ["vmsnapshotid", ]


class deleteVMSnapshotResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

