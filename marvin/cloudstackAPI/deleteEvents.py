"""Delete one or more events."""
from baseCmd import *
from baseResponse import *


class deleteEventsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """end date range to delete events (including) this date (use format "yyyy-MM-dd" or the new format "yyyy-MM-ddThh:mm:ss")"""
        self.enddate = None
        self.typeInfo['enddate'] = 'date'
        """the IDs of the events"""
        self.ids = []
        self.typeInfo['ids'] = 'list'
        """start date range to delete events (including) this date (use format "yyyy-MM-dd" or the new format "yyyy-MM-ddThh:mm:ss")"""
        self.startdate = None
        self.typeInfo['startdate'] = 'date'
        """delete by event type"""
        self.type = None
        self.typeInfo['type'] = 'string'
        self.required = []


class deleteEventsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
