"""Archive one or more alerts."""
from baseCmd import *
from baseResponse import *
class archiveAlertsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """end date range to archive alerts (including) this date (use format "yyyy-MM-dd" or the new format "yyyy-MM-ddThh:mm:ss")"""
        self.enddate = None
        self.typeInfo['enddate'] = 'date'
        """the IDs of the alerts"""
        self.ids = []
        self.typeInfo['ids'] = 'list'
        """start date range to archive alerts (including) this date (use format "yyyy-MM-dd" or the new format "yyyy-MM-ddThh:mm:ss")"""
        self.startdate = None
        self.typeInfo['startdate'] = 'date'
        """archive by alert type"""
        self.type = None
        self.typeInfo['type'] = 'string'
        self.required = []

class archiveAlertsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

