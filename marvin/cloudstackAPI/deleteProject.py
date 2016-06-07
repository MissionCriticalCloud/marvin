"""Deletes a project"""
from baseCmd import *
from baseResponse import *


class deleteProjectCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """id of the project to be deleted"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteProjectResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

