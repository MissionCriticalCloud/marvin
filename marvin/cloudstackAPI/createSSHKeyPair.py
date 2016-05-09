"""Create a new keypair and returns the private key"""
from baseCmd import *
from baseResponse import *


class createSSHKeyPairCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Name of the keypair"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """an optional account for the ssh key. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """an optional domainId for the ssh key. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """an optional project for the ssh key"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["name", ]


class createSSHKeyPairResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """Private key"""
        self.privatekey = None
        self.typeInfo['privatekey'] = 'string'
