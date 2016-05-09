"""Retrieves a cloud identifier."""
from baseCmd import *
from baseResponse import *
class getCloudIdentifierCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the user ID for the cloud identifier"""
        """Required"""
        self.userid = None
        self.typeInfo['userid'] = 'uuid'
        self.required = ["userid",]

class getCloudIdentifierResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the cloud identifier"""
        self.cloudidentifier = None
        self.typeInfo['cloudidentifier'] = 'string'
        """the signed response for the cloud identifier"""
        self.signature = None
        self.typeInfo['signature'] = 'string'
        """the user ID for the cloud identifier"""
        self.userid = None
        self.typeInfo['userid'] = 'string'

