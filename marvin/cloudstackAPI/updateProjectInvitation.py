"""Accepts or declines project invitation"""
from baseCmd import *
from baseResponse import *


class updateProjectInvitationCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """id of the project to join"""
        """Required"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """if true, accept the invitation, decline if false. True by default"""
        self.accept = None
        self.typeInfo['accept'] = 'boolean'
        """account that is joining the project"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list invitations for specified account; this parameter has to be specified with domainId"""
        self.token = None
        self.typeInfo['token'] = 'string'
        self.required = ["projectid", ]


class updateProjectInvitationResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
