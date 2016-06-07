"""Deletes a storage pool."""
from baseCmd import *
from baseResponse import *


class deleteStoragePoolCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Storage pool id"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Force destroy storage pool (force expunge volumes in Destroyed state as a part of pool removal)"""
        self.forced = None
        self.typeInfo['forced'] = 'boolean'
        self.required = ["id", ]


class deleteStoragePoolResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

