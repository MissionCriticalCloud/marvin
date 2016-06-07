"""Deletes a specified domain"""
from baseCmd import *
from baseResponse import *


class deleteDomainCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """ID of domain to delete"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """true if all domain resources (child domains, accounts) have to be cleaned up, false otherwise"""
        self.cleanup = None
        self.typeInfo['cleanup'] = 'boolean'
        self.required = ["id", ]


class deleteDomainResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

