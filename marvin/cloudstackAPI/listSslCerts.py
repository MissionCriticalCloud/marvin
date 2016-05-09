"""Lists SSL certificates"""
from baseCmd import *
from baseResponse import *


class listSslCertsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Account ID"""
        self.accountid = None
        self.typeInfo['accountid'] = 'uuid'
        """ID of SSL certificate"""
        self.certid = None
        self.typeInfo['certid'] = 'uuid'
        """Load balancer rule ID"""
        self.lbruleid = None
        self.typeInfo['lbruleid'] = 'uuid'
        """Project that owns the SSL certificate"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = []


class listSslCertsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """SSL certificate ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """account for the certificate"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """certificate chain"""
        self.certchain = None
        self.typeInfo['certchain'] = 'string'
        """certificate"""
        self.certificate = None
        self.typeInfo['certificate'] = 'string'
        """the domain name of the network owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the network owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """certificate fingerprint"""
        self.fingerprint = None
        self.typeInfo['fingerprint'] = 'string'
        """List of loabalancers this certificate is bound to"""
        self.loadbalancerrulelist = None
        self.typeInfo['loadbalancerrulelist'] = 'list'
        """the project name of the certificate"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the certificate"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
