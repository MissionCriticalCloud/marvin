"""Upgrades router to use newer template"""
from baseCmd import *
from baseResponse import *


class upgradeRouterTemplateCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """upgrades all routers owned by the specified account"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """upgrades all routers within the specified cluster"""
        self.clusterid = None
        self.typeInfo['clusterid'] = 'uuid'
        """upgrades all routers owned by the specified domain"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """upgrades router with the specified Id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """upgrades all routers within the specified pod"""
        self.podid = None
        self.typeInfo['podid'] = 'uuid'
        """upgrades all routers within the specified zone"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = []


class upgradeRouterTemplateResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the UUID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = 'string'
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = 'integer'
