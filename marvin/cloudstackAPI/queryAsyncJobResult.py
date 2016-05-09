"""Retrieves the current status of asynchronous job."""
from baseCmd import *
from baseResponse import *


class queryAsyncJobResultCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the ID of the asychronous job"""
        """Required"""
        self.jobid = None
        self.typeInfo['jobid'] = 'uuid'
        self.required = ["jobid", ]


class queryAsyncJobResultResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the account that executed the async command"""
        self.accountid = None
        self.typeInfo['accountid'] = 'string'
        """the async command executed"""
        self.cmd = None
        self.typeInfo['cmd'] = 'string'
        """the created date of the job"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the unique ID of the instance/entity object related to the job"""
        self.jobinstanceid = None
        self.typeInfo['jobinstanceid'] = 'string'
        """the instance/entity object related to the job"""
        self.jobinstancetype = None
        self.typeInfo['jobinstancetype'] = 'string'
        """the progress information of the PENDING job"""
        self.jobprocstatus = None
        self.typeInfo['jobprocstatus'] = 'integer'
        """the result reason"""
        self.jobresult = None
        self.typeInfo['jobresult'] = 'responseobject'
        """the result code for the job"""
        self.jobresultcode = None
        self.typeInfo['jobresultcode'] = 'integer'
        """the result type"""
        self.jobresulttype = None
        self.typeInfo['jobresulttype'] = 'string'
        """the current job status-should be 0 for PENDING"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = 'integer'
        """the user that executed the async command"""
        self.userid = None
        self.typeInfo['userid'] = 'string'
        """the ID of the async job"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
