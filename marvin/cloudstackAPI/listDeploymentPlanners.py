"""Lists all DeploymentPlanners available."""
from baseCmd import *
from baseResponse import *


class listDeploymentPlannersCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listDeploymentPlannersResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """Deployment Planner name"""
        self.name = None
        self.typeInfo['name'] = 'string'

