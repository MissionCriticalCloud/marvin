"""List template visibility and all accounts that have permissions to view this template."""
from baseCmd import *
from baseResponse import *
class listTemplatePermissionsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the template ID"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id",]

class listTemplatePermissionsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the template ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the list of accounts the template is available for"""
        self.account = None
        self.typeInfo['account'] = 'list'
        """the ID of the domain to which the template belongs"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """true if this template is a public template, false otherwise"""
        self.ispublic = None
        self.typeInfo['ispublic'] = 'boolean'
        """the list of projects the template is available for"""
        self.projectids = None
        self.typeInfo['projectids'] = 'list'

