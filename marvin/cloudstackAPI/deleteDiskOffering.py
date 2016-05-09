"""Updates a disk offering."""
from baseCmd import *
from baseResponse import *
class deleteDiskOfferingCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """ID of the disk offering"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id",]

class deleteDiskOfferingResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

