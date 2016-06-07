"""Deletes a detached disk volume."""
from baseCmd import *
from baseResponse import *


class deleteVolumeCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """The ID of the disk volume"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteVolumeResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

