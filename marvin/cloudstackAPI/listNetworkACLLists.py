"""Lists all network ACLs"""
from baseCmd import *
from baseResponse import *


class listNetworkACLListsCmd(baseCmd):
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
        """Lists network ACL with the specified ID."""
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
        """list network ACLs by specified name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """list network ACLs by network ID"""
        self.networkid = None
        self.typeInfo['networkid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """list network ACLs by VPC ID"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        self.required = []


class listNetworkACLListsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the ACL"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Description of the ACL"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """is ACL for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the Name of the ACL"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Id of the VPC this ACL is associated with"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'
