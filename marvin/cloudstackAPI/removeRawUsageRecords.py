"""Safely removes raw records from cloud_usage table"""
from baseCmd import *
from baseResponse import *


class removeRawUsageRecordsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Specify the number of days (greater than zero) to remove records that are older than those number of days from today. For example, specifying 10 would result in removing all the records created before 10 days from today"""
        """Required"""
        self.interval = None
        self.typeInfo['interval'] = 'integer'
        self.required = ["interval", ]


class removeRawUsageRecordsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

