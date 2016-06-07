"""Configures a virtual router element."""
from baseCmd import *
from baseResponse import *


class configureVirtualRouterElementCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the virtual router provider"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Enabled/Disabled the service provider"""
        """Required"""
        self.enabled = None
        self.typeInfo['enabled'] = 'boolean'
        self.required = ["id", "enabled", ]


class configureVirtualRouterElementResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the router"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the provider"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain associated with the provider"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID associated with the provider"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """Enabled/Disabled the service provider"""
        self.enabled = None
        self.typeInfo['enabled'] = 'boolean'
        """the physical network service provider id of the provider"""
        self.nspid = None
        self.typeInfo['nspid'] = 'string'
        """the project name of the address"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the ipaddress"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'

