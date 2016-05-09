"""Lists dedicated guest vlan ranges"""
from baseCmd import *
from baseResponse import *
class listDedicatedGuestVlanRangesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the account with which the guest VLAN range is associated. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain ID with which the guest VLAN range is associated.  If used with the account parameter, returns all guest VLAN ranges for that account in the specified domain."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """the dedicated guest vlan range"""
        self.guestvlanrange = None
        self.typeInfo['guestvlanrange'] = 'string'
        """list dedicated guest vlan ranges by id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """physical network id of the guest VLAN range"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'uuid'
        """project who will own the guest VLAN range"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """zone of the guest VLAN range"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = []

class listDedicatedGuestVlanRangesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the guest VLAN range"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account of the guest VLAN range"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name of the guest VLAN range"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the guest VLAN range"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the guest VLAN range"""
        self.guestvlanrange = None
        self.typeInfo['guestvlanrange'] = 'string'
        """the physical network of the guest vlan range"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'long'
        """the project name of the guest vlan range"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the guest vlan range"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the zone of the guest vlan range"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'long'

