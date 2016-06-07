"""Generates usage records. This will generate records only if there any records to be generated, i.e if the scheduled usage job was not run or failed"""
from baseCmd import *
from baseResponse import *


class generateUsageRecordsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """End date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-03."""
        """Required"""
        self.enddate = None
        self.typeInfo['enddate'] = 'date'
        """Start date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-01."""
        """Required"""
        self.startdate = None
        self.typeInfo['startdate'] = 'date'
        """List events for the specified domain."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        self.required = ["enddate", "startdate", ]


class generateUsageRecordsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

