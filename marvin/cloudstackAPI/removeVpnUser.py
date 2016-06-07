"""Removes vpn user"""
from baseCmd import *
from baseResponse import *


class removeVpnUserCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """username for the vpn user"""
        """Required"""
        self.username = None
        self.typeInfo['username'] = 'string'
        """an optional account for the vpn user. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """an optional domainId for the vpn user. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """remove vpn user from the project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["username", ]


class removeVpnUserResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

