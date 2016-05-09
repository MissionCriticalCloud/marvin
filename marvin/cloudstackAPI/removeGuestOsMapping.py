"""Removes a Guest OS Mapping."""
from baseCmd import *
from baseResponse import *
class removeGuestOsMappingCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """ID of the guest OS mapping"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id",]

class removeGuestOsMappingResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

