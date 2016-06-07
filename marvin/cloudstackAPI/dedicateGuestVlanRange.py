"""Dedicates a guest vlan range to an account"""
from baseCmd import *
from baseResponse import *


class dedicateGuestVlanRangeCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """account who will own the VLAN"""
        """Required"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """domain ID of the account owning a VLAN"""
        """Required"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """physical network ID of the vlan"""
        """Required"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'uuid'
        """guest vlan range to be dedicated"""
        """Required"""
        self.vlanrange = None
        self.typeInfo['vlanrange'] = 'string'
        """project who will own the VLAN"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["account", "domainid", "physicalnetworkid", "vlanrange", ]


class dedicateGuestVlanRangeResponse (baseResponse):
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

