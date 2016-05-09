"""Upload a certificate to CloudStack"""
from baseCmd import *
from baseResponse import *
class uploadSslCertCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """SSL certificate"""
        """Required"""
        self.certificate = None
        self.typeInfo['certificate'] = 'string'
        """Private key"""
        """Required"""
        self.privatekey = None
        self.typeInfo['privatekey'] = 'string'
        """account that will own the SSL certificate"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """Certificate chain of trust"""
        self.certchain = None
        self.typeInfo['certchain'] = 'string'
        """domain ID of the account owning the SSL certificate"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """Password for the private key"""
        self.password = None
        self.typeInfo['password'] = 'string'
        """an optional project for the SSL certificate"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["certificate","privatekey",]

class uploadSslCertResponse (baseResponse):
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

