"""Updates a vm group"""
from baseCmd import *
from baseResponse import *


class updateInstanceGroupCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Instance group ID"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """new instance group name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        self.required = ["id", ]


class updateInstanceGroupResponse (baseResponse):
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

