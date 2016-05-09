"""Lists vm groups"""
from baseCmd import *
from baseResponse import *


class listInstanceGroupsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list instance groups by ID"""
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
        """list instance groups by name"""
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


class listInstanceGroupsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the instance group"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the instance group"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """time and date the instance group was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the instance group"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the instance group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the name of the instance group"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name of the instance group"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project ID of the instance group"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
