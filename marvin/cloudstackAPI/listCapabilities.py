"""Lists capabilities"""
from baseCmd import *
from baseResponse import *


class listCapabilitiesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        self.required = []


class listCapabilitiesResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """true if regular user is allowed to create projects"""
        self.allowusercreateprojects = None
        self.typeInfo['allowusercreateprojects'] = 'boolean'
        """true if the user can recover and expunge virtualmachines, false otherwise"""
        self.allowuserexpungerecovervm = None
        self.typeInfo['allowuserexpungerecovervm'] = 'boolean'
        """true if the user is allowed to view destroyed virtualmachines, false otherwise"""
        self.allowuserviewdestroyedvm = None
        self.typeInfo['allowuserviewdestroyedvm'] = 'boolean'
        """time interval (in seconds) to reset api count"""
        self.apilimitinterval = None
        self.typeInfo['apilimitinterval'] = 'integer'
        """Max allowed number of api requests within the specified interval"""
        self.apilimitmax = None
        self.typeInfo['apilimitmax'] = 'integer'
        """version of the cloud stack"""
        self.cloudstackversion = None
        self.typeInfo['cloudstackversion'] = 'string'
        """maximum size that can be specified when create disk from disk offering with custom size"""
        self.customdiskofferingmaxsize = None
        self.typeInfo['customdiskofferingmaxsize'] = 'long'
        """minimum size that can be specified when create disk from disk offering with custom size"""
        self.customdiskofferingminsize = None
        self.typeInfo['customdiskofferingminsize'] = 'long'
        """true if snapshot is supported for KVM host, false otherwise"""
        self.kvmsnapshotenabled = None
        self.typeInfo['kvmsnapshotenabled'] = 'boolean'
        """If invitation confirmation is required when add account to project"""
        self.projectinviterequired = None
        self.typeInfo['projectinviterequired'] = 'boolean'
        """true if region wide secondary is enabled, false otherwise"""
        self.regionsecondaryenabled = None
        self.typeInfo['regionsecondaryenabled'] = 'boolean'
        """true if security groups support is enabled, false otherwise"""
        self.securitygroupsenabled = None
        self.typeInfo['securitygroupsenabled'] = 'boolean'
        """true if region supports elastic load balancer on basic zones"""
        self.supportELB = None
        self.typeInfo['supportELB'] = 'string'
        """true if user and domain admins can set templates to be shared, false otherwise"""
        self.userpublictemplateenabled = None
        self.typeInfo['userpublictemplateenabled'] = 'boolean'

