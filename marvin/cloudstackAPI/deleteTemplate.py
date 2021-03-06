"""Deletes a template from the system. All virtual machines using the deleted template will not be affected."""
from baseCmd import *
from baseResponse import *


class deleteTemplateCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the template"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the ID of zone of the template"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["id", ]


class deleteTemplateResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

