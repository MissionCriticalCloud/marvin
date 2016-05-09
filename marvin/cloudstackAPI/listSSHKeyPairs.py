"""List registered keypairs"""
from baseCmd import *
from baseResponse import *


class listSSHKeyPairsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """A public key fingerprint to look for"""
        self.fingerprint = None
        self.typeInfo['fingerprint'] = 'string'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """A key pair name to look for"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = []


class listSSHKeyPairsResponse(baseResponse):
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
