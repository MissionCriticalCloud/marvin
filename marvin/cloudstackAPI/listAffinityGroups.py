"""Lists affinity groups"""
from baseCmd import *
from baseResponse import *
class listAffinityGroupsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list the affinity group by the ID provided"""
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
        """lists affinity groups by name"""
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
        """lists affinity groups by type"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """lists affinity groups by virtual machine ID"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        self.required = []

class listAffinityGroupsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the affinity group"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the affinity group"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the description of the affinity group"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the domain name of the affinity group"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the affinity group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the name of the affinity group"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name of the affinity group"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project ID of the affinity group"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the type of the affinity group"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """virtual machine IDs associated with this affinity group"""
        self.virtualmachineIds = None
        self.typeInfo['virtualmachineIds'] = 'list'

