"""Register a public key in a keypair under a certain name"""
from baseCmd import *
from baseResponse import *


class registerSSHKeyPairCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Name of the keypair"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Public key material of the keypair"""
        """Required"""
        self.publickey = None
        self.typeInfo['publickey'] = 'string'
        """an optional account for the ssh key. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """an optional domainId for the ssh key. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """an optional project for the ssh key"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["name", "publickey", ]


class registerSSHKeyPairResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the owner of the keypair"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name of the keypair owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the keypair owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """Fingerprint of the public key"""
        self.fingerprint = None
        self.typeInfo['fingerprint'] = 'string'
        """Name of the keypair"""
        self.name = None
        self.typeInfo['name'] = 'string'
