"""Creates a snapshot policy for the account."""
from baseCmd import *
from baseResponse import *
class createSnapshotPolicyCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """valid values are HOURLY, DAILY, WEEKLY, and MONTHLY"""
        """Required"""
        self.intervaltype = None
        self.typeInfo['intervaltype'] = 'string'
        """maximum number of snapshots to retain"""
        """Required"""
        self.maxsnaps = None
        self.typeInfo['maxsnaps'] = 'integer'
        """time the snapshot is scheduled to be taken. Format is:* if HOURLY, MM* if DAILY, MM:HH* if WEEKLY, MM:HH:DD (1-7)* if MONTHLY, MM:HH:DD (1-28)"""
        """Required"""
        self.schedule = None
        self.typeInfo['schedule'] = 'string'
        """Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."""
        """Required"""
        self.timezone = None
        self.typeInfo['timezone'] = 'string'
        """the ID of the disk volume"""
        """Required"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'uuid'
        """an optional field, whether to the display the policy to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["intervaltype","maxsnaps","schedule","timezone","volumeid",]

class createSnapshotPolicyResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the snapshot policy"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """is this policy for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the interval type of the snapshot policy"""
        self.intervaltype = None
        self.typeInfo['intervaltype'] = 'short'
        """maximum number of snapshots retained"""
        self.maxsnaps = None
        self.typeInfo['maxsnaps'] = 'int'
        """time the snapshot is scheduled to be taken."""
        self.schedule = None
        self.typeInfo['schedule'] = 'string'
        """the time zone of the snapshot policy"""
        self.timezone = None
        self.typeInfo['timezone'] = 'string'
        """the ID of the disk volume"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'string'

