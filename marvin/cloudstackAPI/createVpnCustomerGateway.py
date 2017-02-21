"""Creates site to site vpn customer gateway"""
from baseCmd import *
from baseResponse import *


class createVpnCustomerGatewayCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """guest cidr list of the customer gateway"""
        """Required"""
        self.cidrlist = []
        self.typeInfo['cidrlist'] = 'list'
        """ESP policy of the customer gateway"""
        """Required"""
        self.esppolicy = None
        self.typeInfo['esppolicy'] = 'string'
        """public ip address id of the customer gateway"""
        """Required"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """IKE policy of the customer gateway"""
        """Required"""
        self.ikepolicy = None
        self.typeInfo['ikepolicy'] = 'string'
        """IPsec Preshared-Key of the customer gateway. Cannot contain newline or double quotes."""
        """Required"""
        self.ipsecpsk = None
        self.typeInfo['ipsecpsk'] = 'string'
        """the account associated with the gateway. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain ID associated with the gateway. If used with the account parameter returns the gateway associated with the account for the specified domain."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """If DPD is enabled for VPN connection"""
        self.dpd = None
        self.typeInfo['dpd'] = 'boolean'
        """Lifetime of phase 2 VPN connection to the customer gateway, in seconds"""
        self.esplifetime = None
        self.typeInfo['esplifetime'] = 'long'
        """Force Encapsulation for NAT traversal"""
        self.forceencap = None
        self.typeInfo['forceencap'] = 'boolean'
        """Lifetime of phase 1 VPN connection to the customer gateway, in seconds"""
        self.ikelifetime = None
        self.typeInfo['ikelifetime'] = 'long'
        """name of this customer gateway"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """create site-to-site VPN customer gateway for the project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["cidrlist", "esppolicy", "gateway", "ikepolicy", "ipsecpsk", ]


class createVpnCustomerGatewayResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the vpn gateway ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """guest cidr list of the customer gateway"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """the domain name of the owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """if DPD is enabled for customer gateway"""
        self.dpd = None
        self.typeInfo['dpd'] = 'boolean'
        """Lifetime of ESP SA of customer gateway"""
        self.esplifetime = None
        self.typeInfo['esplifetime'] = 'long'
        """IPsec policy of customer gateway"""
        self.esppolicy = None
        self.typeInfo['esppolicy'] = 'string'
        """if Force NAT Encapsulation is enabled for customer gateway"""
        self.forceencap = None
        self.typeInfo['forceencap'] = 'boolean'
        """public ip address id of the customer gateway"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """Lifetime of IKE SA of customer gateway"""
        self.ikelifetime = None
        self.typeInfo['ikelifetime'] = 'long'
        """IKE policy of customer gateway"""
        self.ikepolicy = None
        self.typeInfo['ikepolicy'] = 'string'
        """guest ip of the customer gateway"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """IPsec preshared-key of customer gateway"""
        self.ipsecpsk = None
        self.typeInfo['ipsecpsk'] = 'string'
        """name of the customer gateway"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the date and time the host was removed"""
        self.removed = None
        self.typeInfo['removed'] = 'date'

