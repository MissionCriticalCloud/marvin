"""Deletes a keypair by name"""
from baseCmd import *
from baseResponse import *


class deleteSSHKeyPairCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Name of the keypair"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the account associated with the keypair. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain ID associated with the keypair"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """the project associated with keypair"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["name", ]


class deleteSSHKeyPairResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

