"""Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."""
from baseCmd import *
from baseResponse import *


class createAutoScaleVmGroupCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the load balancer rule"""
        """Required"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'uuid'
        """the maximum number of members in the vmgroup, The number of instances in the vm group will be equal to or less than this number."""
        """Required"""
        self.maxmembers = None
        self.typeInfo['maxmembers'] = 'integer'
        """the minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number."""
        """Required"""
        self.minmembers = None
        self.typeInfo['minmembers'] = 'integer'
        """list of scaledown autoscale policies"""
        """Required"""
        self.scaledownpolicyids = []
        self.typeInfo['scaledownpolicyids'] = 'list'
        """list of scaleup autoscale policies"""
        """Required"""
        self.scaleuppolicyids = []
        self.typeInfo['scaleuppolicyids'] = 'list'
        """the autoscale profile that contains information about the vms in the vm group."""
        """Required"""
        self.vmprofileid = None
        self.typeInfo['vmprofileid'] = 'uuid'
        """an optional field, whether to the display the group to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the frequency at which the conditions have to be evaluated"""
        self.interval = None
        self.typeInfo['interval'] = 'integer'
        self.required = ["lbruleid", "maxmembers", "minmembers", "scaledownpolicyids", "scaleuppolicyids", "vmprofileid", ]


class createAutoScaleVmGroupResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the autoscale vm group ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the instance group"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name of the vm profile"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the vm profile"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """is group for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the frequency at which the conditions have to be evaluated"""
        self.interval = None
        self.typeInfo['interval'] = 'int'
        """the load balancer rule ID"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'string'
        """the maximum number of members in the vmgroup, The number of instances in the vm group will be equal to or less than this number."""
        self.maxmembers = None
        self.typeInfo['maxmembers'] = 'int'
        """the minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number."""
        self.minmembers = None
        self.typeInfo['minmembers'] = 'int'
        """the project name of the vm profile"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id vm profile"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """list of scaledown autoscale policies"""
        self.scaledownpolicies = None
        self.typeInfo['scaledownpolicies'] = 'list'
        """list of scaleup autoscale policies"""
        self.scaleuppolicies = None
        self.typeInfo['scaleuppolicies'] = 'list'
        """the current state of the AutoScale Vm Group"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the autoscale profile that contains information about the vms in the vm group."""
        self.vmprofileid = None
        self.typeInfo['vmprofileid'] = 'string'

