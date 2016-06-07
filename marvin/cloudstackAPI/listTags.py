"""List resource tag(s)"""
from baseCmd import *
from baseResponse import *


class listTagsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list by customer name"""
        self.customer = None
        self.typeInfo['customer'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """list by key"""
        self.key = None
        self.typeInfo['key'] = 'string'
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
        """list by resource id"""
        self.resourceid = None
        self.typeInfo['resourceid'] = 'string'
        """list by resource type"""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'
        """list by value"""
        self.value = None
        self.typeInfo['value'] = 'string'
        self.required = []


class listTagsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the account associated with the tag"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """customer associated with the tag"""
        self.customer = None
        self.typeInfo['customer'] = 'string'
        """the domain associated with the tag"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the ID of the domain associated with the tag"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """tag key name"""
        self.key = None
        self.typeInfo['key'] = 'string'
        """the project name where tag belongs to"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id the tag belongs to"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """id of the resource"""
        self.resourceid = None
        self.typeInfo['resourceid'] = 'string'
        """resource type"""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'
        """tag value"""
        self.value = None
        self.typeInfo['value'] = 'string'

