"""Lists site 2 site vpn gateways"""
from baseCmd import *
from baseResponse import *


class listVpnGatewaysCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list resources by display flag; only ROOT admin is eligible to pass this parameter"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """id of the vpn gateway"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """id of vpc"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        self.required = []


class listVpnGatewaysResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the vpn gateway ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name of the owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """is vpn gateway for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the project name"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the public IP address"""
        self.publicip = None
        self.typeInfo['publicip'] = 'string'
        """the date and time the host was removed"""
        self.removed = None
        self.typeInfo['removed'] = 'date'
        """the vpc id of this gateway"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'

