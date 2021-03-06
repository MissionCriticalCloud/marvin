"""Creates an affinity/anti-affinity group"""
from baseCmd import *
from baseResponse import *


class createAffinityGroupCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """name of the affinity group"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Type of the affinity group from the available affinity/anti-affinity group types"""
        """Required"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """an account for the affinity group. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """optional description of the affinity group"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """domainId of the account owning the affinity group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """create affinity group for project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["name", "type", ]


class createAffinityGroupResponse (baseResponse):
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

