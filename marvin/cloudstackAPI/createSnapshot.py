"""Creates an instant snapshot of a volume."""
from baseCmd import *
from baseResponse import *


class createSnapshotCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """The ID of the disk volume"""
        """Required"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'uuid'
        """The account of the snapshot. The account parameter must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """The domain ID of the snapshot. If used with the account parameter, specifies a domain for the account associated with the disk volume."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """the name of the snapshot"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """policy id of the snapshot, if this is null, then use MANUAL_POLICY."""
        self.policyid = None
        self.typeInfo['policyid'] = 'uuid'
        """quiesce vm if true"""
        self.quiescevm = None
        self.typeInfo['quiescevm'] = 'boolean'
        self.required = ["volumeid", ]


class createSnapshotResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """ID of the snapshot"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the snapshot"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the date the snapshot was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the snapshot's account"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the snapshot's account"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """valid types are hourly, daily, weekly, monthy, template, and none."""
        self.intervaltype = None
        self.typeInfo['intervaltype'] = 'string'
        """name of the snapshot"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """physical size of backedup snapshot on image store"""
        self.physicalsize = None
        self.typeInfo['physicalsize'] = 'long'
        """the project name of the snapshot"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the snapshot"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """indicates whether the underlying storage supports reverting the volume to this snapshot"""
        self.revertable = None
        self.typeInfo['revertable'] = 'boolean'
        """the type of the snapshot"""
        self.snapshottype = None
        self.typeInfo['snapshottype'] = 'string'
        """the state of the snapshot. BackedUp means that snapshot is ready to be used; Creating - the snapshot is being allocated on the primary storage; BackingUp - the snapshot is being backed up on secondary storage"""
        self.state = None
        self.typeInfo['state'] = 'state'
        """ID of the disk volume"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'string'
        """name of the disk volume"""
        self.volumename = None
        self.typeInfo['volumename'] = 'string'
        """type of the disk volume"""
        self.volumetype = None
        self.typeInfo['volumetype'] = 'string'
        """id of the availability zone"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the list of resource tags associated with snapshot"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = ''

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

