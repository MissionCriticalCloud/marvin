"""Creates a condition"""
from baseCmd import *
from baseResponse import *


class createConditionCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """ID of the Counter."""
        """Required"""
        self.counterid = None
        self.typeInfo['counterid'] = 'uuid'
        """Relational Operator to be used with threshold."""
        """Required"""
        self.relationaloperator = None
        self.typeInfo['relationaloperator'] = 'string'
        """Threshold value."""
        """Required"""
        self.threshold = None
        self.typeInfo['threshold'] = 'long'
        """the account of the condition. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain ID of the account."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        self.required = ["counterid", "relationaloperator", "threshold", ]


class createConditionResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the Condition"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner of the Condition."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """Details of the Counter."""
        self.counter = None
        self.typeInfo['counter'] = 'list'
        """the domain name of the owner."""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the Condition owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the project name of the Condition"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the Condition."""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """Relational Operator to be used with threshold."""
        self.relationaloperator = None
        self.typeInfo['relationaloperator'] = 'string'
        """Threshold Value for the counter."""
        self.threshold = None
        self.typeInfo['threshold'] = 'long'
        """zone id of counter"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'

