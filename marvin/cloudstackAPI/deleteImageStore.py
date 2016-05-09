"""Deletes an image store or Secondary Storage."""
from baseCmd import *
from baseResponse import *
class deleteImageStoreCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """The image store ID or Secondary Storage ID."""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id",]

class deleteImageStoreResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

