"""Lists resource limits."""
from baseCmd import *
from baseResponse import *
class listResourceLimitsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """Lists resource limits by ID."""
        self.id = None
        self.typeInfo['id'] = 'long'
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
        """Type of resource. Values are 0, 1, 2, 3, 4, 6, 7, 8, 9, 10 and 11. 0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses an account can own. 2 - Volume. Number of disk volumes an account can own. 3 - Snapshot. Number of snapshots an account can own. 4 - Template. Number of templates an account can register/create. 5 - Project. Number of projects an account can own. 6 - Network. Number of networks an account can own. 7 - VPC. Number of VPC an account can own. 8 - CPU. Number of CPU an account can allocate for his resources. 9 - Memory. Amount of RAM an account can allocate for his resources. 10 - PrimaryStorage. Total primary storage space (in GiB) a user can use. 11 - SecondaryStorage. Total secondary storage space (in GiB) a user can use."""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'integer'
        self.required = []

class listResourceLimitsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the account of the resource limit"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name of the resource limit"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the resource limit"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the maximum number of the resource. A -1 means the resource currently has no limit."""
        self.max = None
        self.typeInfo['max'] = 'long'
        """the project name of the resource limit"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the resource limit"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """resource type. Values include 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11. See the resourceType parameter for more information on these values."""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'

