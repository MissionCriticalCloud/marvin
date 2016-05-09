"""Test Client for CloudStack API"""
import copy

from activateProject import activateProjectResponse
from addAccountToProject import addAccountToProjectResponse
from addCluster import addClusterResponse
from addGuestOs import addGuestOsResponse
from addGuestOsMapping import addGuestOsMappingResponse
from addHost import addHostResponse
from addImageStore import addImageStoreResponse
from addImageStoreS3 import addImageStoreS3Response
from addIpToNic import addIpToNicResponse
from addNetworkDevice import addNetworkDeviceResponse
from addNetworkServiceProvider import addNetworkServiceProviderResponse
from addNicToVirtualMachine import addNicToVirtualMachineResponse
from addNiciraNvpDevice import addNiciraNvpDeviceResponse
from addRegion import addRegionResponse
from addResourceDetail import addResourceDetailResponse
from addSecondaryStorage import addSecondaryStorageResponse
from addSwift import addSwiftResponse
from addTrafficMonitor import addTrafficMonitorResponse
from addTrafficType import addTrafficTypeResponse
from addVpnUser import addVpnUserResponse
from archiveAlerts import archiveAlertsResponse
from archiveEvents import archiveEventsResponse
from assignCertToLoadBalancer import assignCertToLoadBalancerResponse
from assignToGlobalLoadBalancerRule import assignToGlobalLoadBalancerRuleResponse
from assignToLoadBalancerRule import assignToLoadBalancerRuleResponse
from assignVirtualMachine import assignVirtualMachineResponse
from associateIpAddress import associateIpAddressResponse
from attachIso import attachIsoResponse
from attachVolume import attachVolumeResponse
from authorizeSecurityGroupEgress import authorizeSecurityGroupEgressResponse
from authorizeSecurityGroupIngress import authorizeSecurityGroupIngressResponse
from cancelHostMaintenance import cancelHostMaintenanceResponse
from cancelStorageMaintenance import cancelStorageMaintenanceResponse
from changeServiceForRouter import changeServiceForRouterResponse
from changeServiceForSystemVm import changeServiceForSystemVmResponse
from changeServiceForVirtualMachine import changeServiceForVirtualMachineResponse
from cleanVMReservations import cleanVMReservationsResponse
from configureInternalLoadBalancerElement import configureInternalLoadBalancerElementResponse
from configureVirtualRouterElement import configureVirtualRouterElementResponse
from copyIso import copyIsoResponse
from copyTemplate import copyTemplateResponse
from createAccount import createAccountResponse
from createAffinityGroup import createAffinityGroupResponse
from createAutoScalePolicy import createAutoScalePolicyResponse
from createAutoScaleVmGroup import createAutoScaleVmGroupResponse
from createAutoScaleVmProfile import createAutoScaleVmProfileResponse
from createCondition import createConditionResponse
from createCounter import createCounterResponse
from createDiskOffering import createDiskOfferingResponse
from createDomain import createDomainResponse
from createEgressFirewallRule import createEgressFirewallRuleResponse
from createFirewallRule import createFirewallRuleResponse
from createGlobalLoadBalancerRule import createGlobalLoadBalancerRuleResponse
from createInstanceGroup import createInstanceGroupResponse
from createInternalLoadBalancerElement import createInternalLoadBalancerElementResponse
from createIpForwardingRule import createIpForwardingRuleResponse
from createLBHealthCheckPolicy import createLBHealthCheckPolicyResponse
from createLBStickinessPolicy import createLBStickinessPolicyResponse
from createLoadBalancer import createLoadBalancerResponse
from createLoadBalancerRule import createLoadBalancerRuleResponse
from createNetwork import createNetworkResponse
from createNetworkACL import createNetworkACLResponse
from createNetworkACLList import createNetworkACLListResponse
from createNetworkOffering import createNetworkOfferingResponse
from createPhysicalNetwork import createPhysicalNetworkResponse
from createPod import createPodResponse
from createPortForwardingRule import createPortForwardingRuleResponse
from createPortableIpRange import createPortableIpRangeResponse
from createPrivateGateway import createPrivateGatewayResponse
from createProject import createProjectResponse
from createRemoteAccessVpn import createRemoteAccessVpnResponse
from createSSHKeyPair import createSSHKeyPairResponse
from createSecondaryStagingStore import createSecondaryStagingStoreResponse
from createSecurityGroup import createSecurityGroupResponse
from createServiceOffering import createServiceOfferingResponse
from createSnapshot import createSnapshotResponse
from createSnapshotPolicy import createSnapshotPolicyResponse
from createStaticRoute import createStaticRouteResponse
from createStorageNetworkIpRange import createStorageNetworkIpRangeResponse
from createStoragePool import createStoragePoolResponse
from createTags import createTagsResponse
from createTemplate import createTemplateResponse
from createUser import createUserResponse
from createVMSnapshot import createVMSnapshotResponse
from createVPC import createVPCResponse
from createVPCOffering import createVPCOfferingResponse
from createVirtualRouterElement import createVirtualRouterElementResponse
from createVlanIpRange import createVlanIpRangeResponse
from createVolume import createVolumeResponse
from createVpnConnection import createVpnConnectionResponse
from createVpnCustomerGateway import createVpnCustomerGatewayResponse
from createVpnGateway import createVpnGatewayResponse
from createZone import createZoneResponse
from dedicateGuestVlanRange import dedicateGuestVlanRangeResponse
from dedicatePublicIpRange import dedicatePublicIpRangeResponse
from deleteAccount import deleteAccountResponse
from deleteAccountFromProject import deleteAccountFromProjectResponse
from deleteAffinityGroup import deleteAffinityGroupResponse
from deleteAlerts import deleteAlertsResponse
from deleteAutoScalePolicy import deleteAutoScalePolicyResponse
from deleteAutoScaleVmGroup import deleteAutoScaleVmGroupResponse
from deleteAutoScaleVmProfile import deleteAutoScaleVmProfileResponse
from deleteCluster import deleteClusterResponse
from deleteCondition import deleteConditionResponse
from deleteCounter import deleteCounterResponse
from deleteDiskOffering import deleteDiskOfferingResponse
from deleteDomain import deleteDomainResponse
from deleteEgressFirewallRule import deleteEgressFirewallRuleResponse
from deleteEvents import deleteEventsResponse
from deleteFirewallRule import deleteFirewallRuleResponse
from deleteGlobalLoadBalancerRule import deleteGlobalLoadBalancerRuleResponse
from deleteHost import deleteHostResponse
from deleteImageStore import deleteImageStoreResponse
from deleteInstanceGroup import deleteInstanceGroupResponse
from deleteIpForwardingRule import deleteIpForwardingRuleResponse
from deleteIso import deleteIsoResponse
from deleteLBHealthCheckPolicy import deleteLBHealthCheckPolicyResponse
from deleteLBStickinessPolicy import deleteLBStickinessPolicyResponse
from deleteLoadBalancer import deleteLoadBalancerResponse
from deleteLoadBalancerRule import deleteLoadBalancerRuleResponse
from deleteNetwork import deleteNetworkResponse
from deleteNetworkACL import deleteNetworkACLResponse
from deleteNetworkACLList import deleteNetworkACLListResponse
from deleteNetworkDevice import deleteNetworkDeviceResponse
from deleteNetworkOffering import deleteNetworkOfferingResponse
from deleteNetworkServiceProvider import deleteNetworkServiceProviderResponse
from deleteNiciraNvpDevice import deleteNiciraNvpDeviceResponse
from deletePhysicalNetwork import deletePhysicalNetworkResponse
from deletePod import deletePodResponse
from deletePortForwardingRule import deletePortForwardingRuleResponse
from deletePortableIpRange import deletePortableIpRangeResponse
from deletePrivateGateway import deletePrivateGatewayResponse
from deleteProject import deleteProjectResponse
from deleteProjectInvitation import deleteProjectInvitationResponse
from deleteRemoteAccessVpn import deleteRemoteAccessVpnResponse
from deleteSSHKeyPair import deleteSSHKeyPairResponse
from deleteSecondaryStagingStore import deleteSecondaryStagingStoreResponse
from deleteSecurityGroup import deleteSecurityGroupResponse
from deleteServiceOffering import deleteServiceOfferingResponse
from deleteSnapshot import deleteSnapshotResponse
from deleteSnapshotPolicies import deleteSnapshotPoliciesResponse
from deleteSslCert import deleteSslCertResponse
from deleteStaticRoute import deleteStaticRouteResponse
from deleteStorageNetworkIpRange import deleteStorageNetworkIpRangeResponse
from deleteStoragePool import deleteStoragePoolResponse
from deleteTags import deleteTagsResponse
from deleteTemplate import deleteTemplateResponse
from deleteTrafficMonitor import deleteTrafficMonitorResponse
from deleteTrafficType import deleteTrafficTypeResponse
from deleteUser import deleteUserResponse
from deleteVMSnapshot import deleteVMSnapshotResponse
from deleteVPC import deleteVPCResponse
from deleteVPCOffering import deleteVPCOfferingResponse
from deleteVlanIpRange import deleteVlanIpRangeResponse
from deleteVolume import deleteVolumeResponse
from deleteVpnConnection import deleteVpnConnectionResponse
from deleteVpnCustomerGateway import deleteVpnCustomerGatewayResponse
from deleteVpnGateway import deleteVpnGatewayResponse
from deleteZone import deleteZoneResponse
from deployVirtualMachine import deployVirtualMachineResponse
from destroyRouter import destroyRouterResponse
from destroySystemVm import destroySystemVmResponse
from destroyVirtualMachine import destroyVirtualMachineResponse
from detachIso import detachIsoResponse
from detachVolume import detachVolumeResponse
from disableAccount import disableAccountResponse
from disableAutoScaleVmGroup import disableAutoScaleVmGroupResponse
from disableStaticNat import disableStaticNatResponse
from disableUser import disableUserResponse
from disassociateIpAddress import disassociateIpAddressResponse
from enableAccount import enableAccountResponse
from enableAutoScaleVmGroup import enableAutoScaleVmGroupResponse
from enableStaticNat import enableStaticNatResponse
from enableStorageMaintenance import enableStorageMaintenanceResponse
from enableUser import enableUserResponse
from expungeVirtualMachine import expungeVirtualMachineResponse
from extractIso import extractIsoResponse
from extractTemplate import extractTemplateResponse
from extractVolume import extractVolumeResponse
from findHostsForMigration import findHostsForMigrationResponse
from findStoragePoolsForMigration import findStoragePoolsForMigrationResponse
from generateAlert import generateAlertResponse
from generateUsageRecords import generateUsageRecordsResponse
from getCloudIdentifier import getCloudIdentifierResponse
from getUploadParamsForTemplate import getUploadParamsForTemplateResponse
from getUploadParamsForVolume import getUploadParamsForVolumeResponse
from getUser import getUserResponse
from getVMPassword import getVMPasswordResponse
from getVirtualMachineUserData import getVirtualMachineUserDataResponse
from listAccounts import listAccountsResponse
from listAffinityGroupTypes import listAffinityGroupTypesResponse
from listAffinityGroups import listAffinityGroupsResponse
from listAlerts import listAlertsResponse
from listAsyncJobs import listAsyncJobsResponse
from listAutoScalePolicies import listAutoScalePoliciesResponse
from listAutoScaleVmGroups import listAutoScaleVmGroupsResponse
from listAutoScaleVmProfiles import listAutoScaleVmProfilesResponse
from listCapabilities import listCapabilitiesResponse
from listCapacity import listCapacityResponse
from listClusters import listClustersResponse
from listConditions import listConditionsResponse
from listConfigurations import listConfigurationsResponse
from listCounters import listCountersResponse
from listDedicatedGuestVlanRanges import listDedicatedGuestVlanRangesResponse
from listDeploymentPlanners import listDeploymentPlannersResponse
from listDiskOfferings import listDiskOfferingsResponse
from listDomainChildren import listDomainChildrenResponse
from listDomains import listDomainsResponse
from listEgressFirewallRules import listEgressFirewallRulesResponse
from listEventTypes import listEventTypesResponse
from listEvents import listEventsResponse
from listFirewallRules import listFirewallRulesResponse
from listGlobalLoadBalancerRules import listGlobalLoadBalancerRulesResponse
from listGuestOsMapping import listGuestOsMappingResponse
from listHostTags import listHostTagsResponse
from listHosts import listHostsResponse
from listHypervisorCapabilities import listHypervisorCapabilitiesResponse
from listHypervisors import listHypervisorsResponse
from listImageStores import listImageStoresResponse
from listInstanceGroups import listInstanceGroupsResponse
from listInternalLoadBalancerElements import listInternalLoadBalancerElementsResponse
from listInternalLoadBalancerVMs import listInternalLoadBalancerVMsResponse
from listIpForwardingRules import listIpForwardingRulesResponse
from listIsoPermissions import listIsoPermissionsResponse
from listIsos import listIsosResponse
from listLBHealthCheckPolicies import listLBHealthCheckPoliciesResponse
from listLBStickinessPolicies import listLBStickinessPoliciesResponse
from listLoadBalancerRuleInstances import listLoadBalancerRuleInstancesResponse
from listLoadBalancerRules import listLoadBalancerRulesResponse
from listLoadBalancers import listLoadBalancersResponse
from listNetworkACLLists import listNetworkACLListsResponse
from listNetworkACLs import listNetworkACLsResponse
from listNetworkDevice import listNetworkDeviceResponse
from listNetworkIsolationMethods import listNetworkIsolationMethodsResponse
from listNetworkOfferings import listNetworkOfferingsResponse
from listNetworkServiceProviders import listNetworkServiceProvidersResponse
from listNetworks import listNetworksResponse
from listNiciraNvpDeviceNetworks import listNiciraNvpDeviceNetworksResponse
from listNiciraNvpDevices import listNiciraNvpDevicesResponse
from listNics import listNicsResponse
from listOsCategories import listOsCategoriesResponse
from listOsTypes import listOsTypesResponse
from listPhysicalNetworks import listPhysicalNetworksResponse
from listPods import listPodsResponse
from listPortForwardingRules import listPortForwardingRulesResponse
from listPortableIpRanges import listPortableIpRangesResponse
from listPrivateGateways import listPrivateGatewaysResponse
from listProjectAccounts import listProjectAccountsResponse
from listProjectInvitations import listProjectInvitationsResponse
from listProjects import listProjectsResponse
from listPublicIpAddresses import listPublicIpAddressesResponse
from listRegions import listRegionsResponse
from listRemoteAccessVpns import listRemoteAccessVpnsResponse
from listResourceDetails import listResourceDetailsResponse
from listResourceLimits import listResourceLimitsResponse
from listRouters import listRoutersResponse
from listSSHKeyPairs import listSSHKeyPairsResponse
from listSecondaryStagingStores import listSecondaryStagingStoresResponse
from listSecurityGroups import listSecurityGroupsResponse
from listServiceOfferings import listServiceOfferingsResponse
from listSnapshotPolicies import listSnapshotPoliciesResponse
from listSnapshots import listSnapshotsResponse
from listSslCerts import listSslCertsResponse
from listStaticRoutes import listStaticRoutesResponse
from listStorageNetworkIpRange import listStorageNetworkIpRangeResponse
from listStoragePools import listStoragePoolsResponse
from listStorageProviders import listStorageProvidersResponse
from listStorageTags import listStorageTagsResponse
from listSupportedNetworkServices import listSupportedNetworkServicesResponse
from listSwifts import listSwiftsResponse
from listSystemVms import listSystemVmsResponse
from listTags import listTagsResponse
from listTemplatePermissions import listTemplatePermissionsResponse
from listTemplates import listTemplatesResponse
from listTrafficMonitors import listTrafficMonitorsResponse
from listTrafficTypeImplementors import listTrafficTypeImplementorsResponse
from listTrafficTypes import listTrafficTypesResponse
from listUsageRecords import listUsageRecordsResponse
from listUsageTypes import listUsageTypesResponse
from listUsers import listUsersResponse
from listVMSnapshot import listVMSnapshotResponse
from listVPCOfferings import listVPCOfferingsResponse
from listVPCs import listVPCsResponse
from listVirtualMachines import listVirtualMachinesResponse
from listVirtualRouterElements import listVirtualRouterElementsResponse
from listVlanIpRanges import listVlanIpRangesResponse
from listVolumes import listVolumesResponse
from listVpnConnections import listVpnConnectionsResponse
from listVpnCustomerGateways import listVpnCustomerGatewaysResponse
from listVpnGateways import listVpnGatewaysResponse
from listVpnUsers import listVpnUsersResponse
from listZones import listZonesResponse
from lockAccount import lockAccountResponse
from lockUser import lockUserResponse
from login import loginResponse
from logout import logoutResponse
from markDefaultZoneForAccount import markDefaultZoneForAccountResponse
from migrateSystemVm import migrateSystemVmResponse
from migrateVirtualMachine import migrateVirtualMachineResponse
from migrateVirtualMachineWithVolume import migrateVirtualMachineWithVolumeResponse
from migrateVolume import migrateVolumeResponse
from prepareHostForMaintenance import prepareHostForMaintenanceResponse
from prepareTemplate import prepareTemplateResponse
from queryAsyncJobResult import queryAsyncJobResultResponse
from rebootRouter import rebootRouterResponse
from rebootSystemVm import rebootSystemVmResponse
from rebootVirtualMachine import rebootVirtualMachineResponse
from reconnectHost import reconnectHostResponse
from recoverVirtualMachine import recoverVirtualMachineResponse
from registerIso import registerIsoResponse
from registerSSHKeyPair import registerSSHKeyPairResponse
from registerTemplate import registerTemplateResponse
from registerUserKeys import registerUserKeysResponse
from releaseDedicatedGuestVlanRange import releaseDedicatedGuestVlanRangeResponse
from releaseHostReservation import releaseHostReservationResponse
from releasePublicIpRange import releasePublicIpRangeResponse
from removeCertFromLoadBalancer import removeCertFromLoadBalancerResponse
from removeFromGlobalLoadBalancerRule import removeFromGlobalLoadBalancerRuleResponse
from removeFromLoadBalancerRule import removeFromLoadBalancerRuleResponse
from removeGuestOs import removeGuestOsResponse
from removeGuestOsMapping import removeGuestOsMappingResponse
from removeIpFromNic import removeIpFromNicResponse
from removeNicFromVirtualMachine import removeNicFromVirtualMachineResponse
from removeRawUsageRecords import removeRawUsageRecordsResponse
from removeRegion import removeRegionResponse
from removeResourceDetail import removeResourceDetailResponse
from removeVpnUser import removeVpnUserResponse
from replaceNetworkACLList import replaceNetworkACLListResponse
from resetPasswordForVirtualMachine import resetPasswordForVirtualMachineResponse
from resetSSHKeyForVirtualMachine import resetSSHKeyForVirtualMachineResponse
from resetVpnConnection import resetVpnConnectionResponse
from resizeVolume import resizeVolumeResponse
from restartNetwork import restartNetworkResponse
from restartVPC import restartVPCResponse
from restoreVirtualMachine import restoreVirtualMachineResponse
from revertSnapshot import revertSnapshotResponse
from revertToVMSnapshot import revertToVMSnapshotResponse
from revokeSecurityGroupEgress import revokeSecurityGroupEgressResponse
from revokeSecurityGroupIngress import revokeSecurityGroupIngressResponse
from scaleSystemVm import scaleSystemVmResponse
from scaleVirtualMachine import scaleVirtualMachineResponse
from startInternalLoadBalancerVM import startInternalLoadBalancerVMResponse
from startRouter import startRouterResponse
from startSystemVm import startSystemVmResponse
from startVirtualMachine import startVirtualMachineResponse
from stopInternalLoadBalancerVM import stopInternalLoadBalancerVMResponse
from stopRouter import stopRouterResponse
from stopSystemVm import stopSystemVmResponse
from stopVirtualMachine import stopVirtualMachineResponse
from suspendProject import suspendProjectResponse
from updateAccount import updateAccountResponse
from updateAutoScalePolicy import updateAutoScalePolicyResponse
from updateAutoScaleVmGroup import updateAutoScaleVmGroupResponse
from updateAutoScaleVmProfile import updateAutoScaleVmProfileResponse
from updateCloudToUseObjectStore import updateCloudToUseObjectStoreResponse
from updateCluster import updateClusterResponse
from updateConfiguration import updateConfigurationResponse
from updateDefaultNicForVirtualMachine import updateDefaultNicForVirtualMachineResponse
from updateDiskOffering import updateDiskOfferingResponse
from updateDomain import updateDomainResponse
from updateEgressFirewallRule import updateEgressFirewallRuleResponse
from updateFirewallRule import updateFirewallRuleResponse
from updateGlobalLoadBalancerRule import updateGlobalLoadBalancerRuleResponse
from updateGuestOs import updateGuestOsResponse
from updateGuestOsMapping import updateGuestOsMappingResponse
from updateHost import updateHostResponse
from updateHostPassword import updateHostPasswordResponse
from updateHypervisorCapabilities import updateHypervisorCapabilitiesResponse
from updateInstanceGroup import updateInstanceGroupResponse
from updateIpAddress import updateIpAddressResponse
from updateIso import updateIsoResponse
from updateIsoPermissions import updateIsoPermissionsResponse
from updateLBHealthCheckPolicy import updateLBHealthCheckPolicyResponse
from updateLBStickinessPolicy import updateLBStickinessPolicyResponse
from updateLoadBalancer import updateLoadBalancerResponse
from updateLoadBalancerRule import updateLoadBalancerRuleResponse
from updateNetwork import updateNetworkResponse
from updateNetworkACLItem import updateNetworkACLItemResponse
from updateNetworkACLList import updateNetworkACLListResponse
from updateNetworkOffering import updateNetworkOfferingResponse
from updateNetworkServiceProvider import updateNetworkServiceProviderResponse
from updatePhysicalNetwork import updatePhysicalNetworkResponse
from updatePod import updatePodResponse
from updatePortForwardingRule import updatePortForwardingRuleResponse
from updateProject import updateProjectResponse
from updateProjectInvitation import updateProjectInvitationResponse
from updateRegion import updateRegionResponse
from updateRemoteAccessVpn import updateRemoteAccessVpnResponse
from updateResourceCount import updateResourceCountResponse
from updateResourceLimit import updateResourceLimitResponse
from updateServiceOffering import updateServiceOfferingResponse
from updateSnapshotPolicy import updateSnapshotPolicyResponse
from updateStorageNetworkIpRange import updateStorageNetworkIpRangeResponse
from updateStoragePool import updateStoragePoolResponse
from updateTemplate import updateTemplateResponse
from updateTemplatePermissions import updateTemplatePermissionsResponse
from updateTrafficType import updateTrafficTypeResponse
from updateUser import updateUserResponse
from updateVMAffinityGroup import updateVMAffinityGroupResponse
from updateVPC import updateVPCResponse
from updateVPCOffering import updateVPCOfferingResponse
from updateVirtualMachine import updateVirtualMachineResponse
from updateVmNicIp import updateVmNicIpResponse
from updateVolume import updateVolumeResponse
from updateVpnConnection import updateVpnConnectionResponse
from updateVpnCustomerGateway import updateVpnCustomerGatewayResponse
from updateVpnGateway import updateVpnGatewayResponse
from updateZone import updateZoneResponse
from upgradeRouterTemplate import upgradeRouterTemplateResponse
from uploadCustomCertificate import uploadCustomCertificateResponse
from uploadSslCert import uploadSslCertResponse
from uploadVolume import uploadVolumeResponse


class CloudStackAPIClient(object):
    def __init__(self, connection):
        self.connection = connection
        self._id = None

    def __copy__(self):
        return CloudStackAPIClient(copy.copy(self.connection))

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, identifier):
        self._id = identifier

    def login(self, command, method="GET"):
        response = loginResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def logout(self, command, method="GET"):
        response = logoutResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createAccount(self, command, method="GET"):
        response = createAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAccount(self, command, method="GET"):
        response = deleteAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateAccount(self, command, method="GET"):
        response = updateAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def disableAccount(self, command, method="GET"):
        response = disableAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def enableAccount(self, command, method="GET"):
        response = enableAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def lockAccount(self, command, method="GET"):
        response = lockAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAccounts(self, command, method="GET"):
        response = listAccountsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def markDefaultZoneForAccount(self, command, method="GET"):
        response = markDefaultZoneForAccountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createUser(self, command, method="GET"):
        response = createUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteUser(self, command, method="GET"):
        response = deleteUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateUser(self, command, method="GET"):
        response = updateUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listUsers(self, command, method="GET"):
        response = listUsersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def lockUser(self, command, method="GET"):
        response = lockUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def disableUser(self, command, method="GET"):
        response = disableUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def enableUser(self, command, method="GET"):
        response = enableUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def getUser(self, command, method="GET"):
        response = getUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createDomain(self, command, method="GET"):
        response = createDomainResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateDomain(self, command, method="GET"):
        response = updateDomainResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteDomain(self, command, method="GET"):
        response = deleteDomainResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listDomains(self, command, method="GET"):
        response = listDomainsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listDomainChildren(self, command, method="GET"):
        response = listDomainChildrenResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def getCloudIdentifier(self, command, method="GET"):
        response = getCloudIdentifierResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateResourceLimit(self, command, method="GET"):
        response = updateResourceLimitResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateResourceCount(self, command, method="GET"):
        response = updateResourceCountResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listResourceLimits(self, command, method="GET"):
        response = listResourceLimitsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deployVirtualMachine(self, command, method="GET"):
        response = deployVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def destroyVirtualMachine(self, command, method="GET"):
        response = destroyVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def rebootVirtualMachine(self, command, method="GET"):
        response = rebootVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def startVirtualMachine(self, command, method="GET"):
        response = startVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def stopVirtualMachine(self, command, method="GET"):
        response = stopVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def resetPasswordForVirtualMachine(self, command, method="GET"):
        response = resetPasswordForVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def resetSSHKeyForVirtualMachine(self, command, method="GET"):
        response = resetSSHKeyForVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVirtualMachine(self, command, method="GET"):
        response = updateVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVirtualMachines(self, command, method="GET"):
        response = listVirtualMachinesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def getVMPassword(self, command, method="GET"):
        response = getVMPasswordResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def restoreVirtualMachine(self, command, method="GET"):
        response = restoreVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def changeServiceForVirtualMachine(self, command, method="GET"):
        response = changeServiceForVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def scaleVirtualMachine(self, command, method="GET"):
        response = scaleVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def assignVirtualMachine(self, command, method="GET"):
        response = assignVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def migrateVirtualMachine(self, command, method="GET"):
        response = migrateVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def migrateVirtualMachineWithVolume(self, command, method="GET"):
        response = migrateVirtualMachineWithVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def recoverVirtualMachine(self, command, method="GET"):
        response = recoverVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def expungeVirtualMachine(self, command, method="GET"):
        response = expungeVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def getVirtualMachineUserData(self, command, method="GET"):
        response = getVirtualMachineUserDataResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createSnapshot(self, command, method="GET"):
        response = createSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSnapshots(self, command, method="GET"):
        response = listSnapshotsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteSnapshot(self, command, method="GET"):
        response = deleteSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createSnapshotPolicy(self, command, method="GET"):
        response = createSnapshotPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateSnapshotPolicy(self, command, method="GET"):
        response = updateSnapshotPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteSnapshotPolicies(self, command, method="GET"):
        response = deleteSnapshotPoliciesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSnapshotPolicies(self, command, method="GET"):
        response = listSnapshotPoliciesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def revertSnapshot(self, command, method="GET"):
        response = revertSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createTemplate(self, command, method="GET"):
        response = createTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def registerTemplate(self, command, method="GET"):
        response = registerTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateTemplate(self, command, method="GET"):
        response = updateTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def copyTemplate(self, command, method="GET"):
        response = copyTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteTemplate(self, command, method="GET"):
        response = deleteTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listTemplates(self, command, method="GET"):
        response = listTemplatesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateTemplatePermissions(self, command, method="GET"):
        response = updateTemplatePermissionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listTemplatePermissions(self, command, method="GET"):
        response = listTemplatePermissionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def extractTemplate(self, command, method="GET"):
        response = extractTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def prepareTemplate(self, command, method="GET"):
        response = prepareTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def attachIso(self, command, method="GET"):
        response = attachIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def detachIso(self, command, method="GET"):
        response = detachIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listIsos(self, command, method="GET"):
        response = listIsosResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def registerIso(self, command, method="GET"):
        response = registerIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateIso(self, command, method="GET"):
        response = updateIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteIso(self, command, method="GET"):
        response = deleteIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def copyIso(self, command, method="GET"):
        response = copyIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateIsoPermissions(self, command, method="GET"):
        response = updateIsoPermissionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listIsoPermissions(self, command, method="GET"):
        response = listIsoPermissionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def extractIso(self, command, method="GET"):
        response = extractIsoResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listOsTypes(self, command, method="GET"):
        response = listOsTypesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listOsCategories(self, command, method="GET"):
        response = listOsCategoriesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addGuestOs(self, command, method="GET"):
        response = addGuestOsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateGuestOs(self, command, method="GET"):
        response = updateGuestOsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeGuestOs(self, command, method="GET"):
        response = removeGuestOsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listGuestOsMapping(self, command, method="GET"):
        response = listGuestOsMappingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addGuestOsMapping(self, command, method="GET"):
        response = addGuestOsMappingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateGuestOsMapping(self, command, method="GET"):
        response = updateGuestOsMappingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeGuestOsMapping(self, command, method="GET"):
        response = removeGuestOsMappingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createServiceOffering(self, command, method="GET"):
        response = createServiceOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteServiceOffering(self, command, method="GET"):
        response = deleteServiceOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateServiceOffering(self, command, method="GET"):
        response = updateServiceOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listServiceOfferings(self, command, method="GET"):
        response = listServiceOfferingsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createDiskOffering(self, command, method="GET"):
        response = createDiskOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateDiskOffering(self, command, method="GET"):
        response = updateDiskOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteDiskOffering(self, command, method="GET"):
        response = deleteDiskOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listDiskOfferings(self, command, method="GET"):
        response = listDiskOfferingsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVlanIpRange(self, command, method="GET"):
        response = createVlanIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVlanIpRange(self, command, method="GET"):
        response = deleteVlanIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVlanIpRanges(self, command, method="GET"):
        response = listVlanIpRangesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def dedicatePublicIpRange(self, command, method="GET"):
        response = dedicatePublicIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def releasePublicIpRange(self, command, method="GET"):
        response = releasePublicIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def dedicateGuestVlanRange(self, command, method="GET"):
        response = dedicateGuestVlanRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def releaseDedicatedGuestVlanRange(self, command, method="GET"):
        response = releaseDedicatedGuestVlanRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listDedicatedGuestVlanRanges(self, command, method="GET"):
        response = listDedicatedGuestVlanRangesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def associateIpAddress(self, command, method="GET"):
        response = associateIpAddressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def disassociateIpAddress(self, command, method="GET"):
        response = disassociateIpAddressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listPublicIpAddresses(self, command, method="GET"):
        response = listPublicIpAddressesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateIpAddress(self, command, method="GET"):
        response = updateIpAddressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listPortForwardingRules(self, command, method="GET"):
        response = listPortForwardingRulesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createPortForwardingRule(self, command, method="GET"):
        response = createPortForwardingRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deletePortForwardingRule(self, command, method="GET"):
        response = deletePortForwardingRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updatePortForwardingRule(self, command, method="GET"):
        response = updatePortForwardingRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def enableStaticNat(self, command, method="GET"):
        response = enableStaticNatResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createIpForwardingRule(self, command, method="GET"):
        response = createIpForwardingRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteIpForwardingRule(self, command, method="GET"):
        response = deleteIpForwardingRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listIpForwardingRules(self, command, method="GET"):
        response = listIpForwardingRulesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def disableStaticNat(self, command, method="GET"):
        response = disableStaticNatResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createLoadBalancerRule(self, command, method="GET"):
        response = createLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteLoadBalancerRule(self, command, method="GET"):
        response = deleteLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeFromLoadBalancerRule(self, command, method="GET"):
        response = removeFromLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def assignToLoadBalancerRule(self, command, method="GET"):
        response = assignToLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createLBStickinessPolicy(self, command, method="GET"):
        response = createLBStickinessPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateLBStickinessPolicy(self, command, method="GET"):
        response = updateLBStickinessPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteLBStickinessPolicy(self, command, method="GET"):
        response = deleteLBStickinessPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listLoadBalancerRules(self, command, method="GET"):
        response = listLoadBalancerRulesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listLBStickinessPolicies(self, command, method="GET"):
        response = listLBStickinessPoliciesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listLBHealthCheckPolicies(self, command, method="GET"):
        response = listLBHealthCheckPoliciesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createLBHealthCheckPolicy(self, command, method="GET"):
        response = createLBHealthCheckPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateLBHealthCheckPolicy(self, command, method="GET"):
        response = updateLBHealthCheckPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteLBHealthCheckPolicy(self, command, method="GET"):
        response = deleteLBHealthCheckPolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listLoadBalancerRuleInstances(self, command, method="GET"):
        response = listLoadBalancerRuleInstancesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateLoadBalancerRule(self, command, method="GET"):
        response = updateLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def uploadSslCert(self, command, method="GET"):
        response = uploadSslCertResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteSslCert(self, command, method="GET"):
        response = deleteSslCertResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSslCerts(self, command, method="GET"):
        response = listSslCertsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def assignCertToLoadBalancer(self, command, method="GET"):
        response = assignCertToLoadBalancerResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeCertFromLoadBalancer(self, command, method="GET"):
        response = removeCertFromLoadBalancerResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createCounter(self, command, method="GET"):
        response = createCounterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createCondition(self, command, method="GET"):
        response = createConditionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createAutoScalePolicy(self, command, method="GET"):
        response = createAutoScalePolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createAutoScaleVmProfile(self, command, method="GET"):
        response = createAutoScaleVmProfileResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createAutoScaleVmGroup(self, command, method="GET"):
        response = createAutoScaleVmGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteCounter(self, command, method="GET"):
        response = deleteCounterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteCondition(self, command, method="GET"):
        response = deleteConditionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAutoScalePolicy(self, command, method="GET"):
        response = deleteAutoScalePolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAutoScaleVmProfile(self, command, method="GET"):
        response = deleteAutoScaleVmProfileResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAutoScaleVmGroup(self, command, method="GET"):
        response = deleteAutoScaleVmGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listCounters(self, command, method="GET"):
        response = listCountersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listConditions(self, command, method="GET"):
        response = listConditionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAutoScalePolicies(self, command, method="GET"):
        response = listAutoScalePoliciesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAutoScaleVmProfiles(self, command, method="GET"):
        response = listAutoScaleVmProfilesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAutoScaleVmGroups(self, command, method="GET"):
        response = listAutoScaleVmGroupsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def enableAutoScaleVmGroup(self, command, method="GET"):
        response = enableAutoScaleVmGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def disableAutoScaleVmGroup(self, command, method="GET"):
        response = disableAutoScaleVmGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateAutoScalePolicy(self, command, method="GET"):
        response = updateAutoScalePolicyResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateAutoScaleVmProfile(self, command, method="GET"):
        response = updateAutoScaleVmProfileResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateAutoScaleVmGroup(self, command, method="GET"):
        response = updateAutoScaleVmGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def startRouter(self, command, method="GET"):
        response = startRouterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def rebootRouter(self, command, method="GET"):
        response = rebootRouterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def stopRouter(self, command, method="GET"):
        response = stopRouterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def destroyRouter(self, command, method="GET"):
        response = destroyRouterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def changeServiceForRouter(self, command, method="GET"):
        response = changeServiceForRouterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listRouters(self, command, method="GET"):
        response = listRoutersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVirtualRouterElements(self, command, method="GET"):
        response = listVirtualRouterElementsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def configureVirtualRouterElement(self, command, method="GET"):
        response = configureVirtualRouterElementResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVirtualRouterElement(self, command, method="GET"):
        response = createVirtualRouterElementResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def upgradeRouterTemplate(self, command, method="GET"):
        response = upgradeRouterTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def startSystemVm(self, command, method="GET"):
        response = startSystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def rebootSystemVm(self, command, method="GET"):
        response = rebootSystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def stopSystemVm(self, command, method="GET"):
        response = stopSystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def destroySystemVm(self, command, method="GET"):
        response = destroySystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSystemVms(self, command, method="GET"):
        response = listSystemVmsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def migrateSystemVm(self, command, method="GET"):
        response = migrateSystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def changeServiceForSystemVm(self, command, method="GET"):
        response = changeServiceForSystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def scaleSystemVm(self, command, method="GET"):
        response = scaleSystemVmResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateConfiguration(self, command, method="GET"):
        response = updateConfigurationResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listConfigurations(self, command, method="GET"):
        response = listConfigurationsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listCapabilities(self, command, method="GET"):
        response = listCapabilitiesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listDeploymentPlanners(self, command, method="GET"):
        response = listDeploymentPlannersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def cleanVMReservations(self, command, method="GET"):
        response = cleanVMReservationsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createPod(self, command, method="GET"):
        response = createPodResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updatePod(self, command, method="GET"):
        response = updatePodResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deletePod(self, command, method="GET"):
        response = deletePodResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listPods(self, command, method="GET"):
        response = listPodsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createZone(self, command, method="GET"):
        response = createZoneResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateZone(self, command, method="GET"):
        response = updateZoneResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteZone(self, command, method="GET"):
        response = deleteZoneResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listZones(self, command, method="GET"):
        response = listZonesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listEvents(self, command, method="GET"):
        response = listEventsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listEventTypes(self, command, method="GET"):
        response = listEventTypesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def archiveEvents(self, command, method="GET"):
        response = archiveEventsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteEvents(self, command, method="GET"):
        response = deleteEventsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAlerts(self, command, method="GET"):
        response = listAlertsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def archiveAlerts(self, command, method="GET"):
        response = archiveAlertsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAlerts(self, command, method="GET"):
        response = deleteAlertsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def generateAlert(self, command, method="GET"):
        response = generateAlertResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listCapacity(self, command, method="GET"):
        response = listCapacityResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addSwift(self, command, method="GET"):
        response = addSwiftResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSwifts(self, command, method="GET"):
        response = listSwiftsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addImageStore(self, command, method="GET"):
        response = addImageStoreResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addImageStoreS3(self, command, method="GET"):
        response = addImageStoreS3Response()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listImageStores(self, command, method="GET"):
        response = listImageStoresResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteImageStore(self, command, method="GET"):
        response = deleteImageStoreResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createSecondaryStagingStore(self, command, method="GET"):
        response = createSecondaryStagingStoreResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSecondaryStagingStores(self, command, method="GET"):
        response = listSecondaryStagingStoresResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteSecondaryStagingStore(self, command, method="GET"):
        response = deleteSecondaryStagingStoreResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateCloudToUseObjectStore(self, command, method="GET"):
        response = updateCloudToUseObjectStoreResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addHost(self, command, method="GET"):
        response = addHostResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addCluster(self, command, method="GET"):
        response = addClusterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteCluster(self, command, method="GET"):
        response = deleteClusterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateCluster(self, command, method="GET"):
        response = updateClusterResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def reconnectHost(self, command, method="GET"):
        response = reconnectHostResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateHost(self, command, method="GET"):
        response = updateHostResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteHost(self, command, method="GET"):
        response = deleteHostResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def prepareHostForMaintenance(self, command, method="GET"):
        response = prepareHostForMaintenanceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def cancelHostMaintenance(self, command, method="GET"):
        response = cancelHostMaintenanceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listHosts(self, command, method="GET"):
        response = listHostsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listHostTags(self, command, method="GET"):
        response = listHostTagsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def findHostsForMigration(self, command, method="GET"):
        response = findHostsForMigrationResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addSecondaryStorage(self, command, method="GET"):
        response = addSecondaryStorageResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateHostPassword(self, command, method="GET"):
        response = updateHostPasswordResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def releaseHostReservation(self, command, method="GET"):
        response = releaseHostReservationResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def attachVolume(self, command, method="GET"):
        response = attachVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def uploadVolume(self, command, method="GET"):
        response = uploadVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def detachVolume(self, command, method="GET"):
        response = detachVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVolume(self, command, method="GET"):
        response = createVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVolume(self, command, method="GET"):
        response = deleteVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVolumes(self, command, method="GET"):
        response = listVolumesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def extractVolume(self, command, method="GET"):
        response = extractVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def migrateVolume(self, command, method="GET"):
        response = migrateVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def resizeVolume(self, command, method="GET"):
        response = resizeVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVolume(self, command, method="GET"):
        response = updateVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def registerUserKeys(self, command, method="GET"):
        response = registerUserKeysResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def queryAsyncJobResult(self, command, method="GET"):
        response = queryAsyncJobResultResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAsyncJobs(self, command, method="GET"):
        response = listAsyncJobsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listStoragePools(self, command, method="GET"):
        response = listStoragePoolsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listStorageProviders(self, command, method="GET"):
        response = listStorageProvidersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listStorageTags(self, command, method="GET"):
        response = listStorageTagsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createStoragePool(self, command, method="GET"):
        response = createStoragePoolResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateStoragePool(self, command, method="GET"):
        response = updateStoragePoolResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteStoragePool(self, command, method="GET"):
        response = deleteStoragePoolResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listClusters(self, command, method="GET"):
        response = listClustersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def enableStorageMaintenance(self, command, method="GET"):
        response = enableStorageMaintenanceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def cancelStorageMaintenance(self, command, method="GET"):
        response = cancelStorageMaintenanceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def findStoragePoolsForMigration(self, command, method="GET"):
        response = findStoragePoolsForMigrationResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createSecurityGroup(self, command, method="GET"):
        response = createSecurityGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteSecurityGroup(self, command, method="GET"):
        response = deleteSecurityGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def authorizeSecurityGroupIngress(self, command, method="GET"):
        response = authorizeSecurityGroupIngressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def revokeSecurityGroupIngress(self, command, method="GET"):
        response = revokeSecurityGroupIngressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def authorizeSecurityGroupEgress(self, command, method="GET"):
        response = authorizeSecurityGroupEgressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def revokeSecurityGroupEgress(self, command, method="GET"):
        response = revokeSecurityGroupEgressResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSecurityGroups(self, command, method="GET"):
        response = listSecurityGroupsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createInstanceGroup(self, command, method="GET"):
        response = createInstanceGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteInstanceGroup(self, command, method="GET"):
        response = deleteInstanceGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateInstanceGroup(self, command, method="GET"):
        response = updateInstanceGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listInstanceGroups(self, command, method="GET"):
        response = listInstanceGroupsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def uploadCustomCertificate(self, command, method="GET"):
        response = uploadCustomCertificateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listHypervisors(self, command, method="GET"):
        response = listHypervisorsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createRemoteAccessVpn(self, command, method="GET"):
        response = createRemoteAccessVpnResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteRemoteAccessVpn(self, command, method="GET"):
        response = deleteRemoteAccessVpnResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listRemoteAccessVpns(self, command, method="GET"):
        response = listRemoteAccessVpnsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateRemoteAccessVpn(self, command, method="GET"):
        response = updateRemoteAccessVpnResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addVpnUser(self, command, method="GET"):
        response = addVpnUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeVpnUser(self, command, method="GET"):
        response = removeVpnUserResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVpnUsers(self, command, method="GET"):
        response = listVpnUsersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createNetworkOffering(self, command, method="GET"):
        response = createNetworkOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateNetworkOffering(self, command, method="GET"):
        response = updateNetworkOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNetworkOffering(self, command, method="GET"):
        response = deleteNetworkOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworkOfferings(self, command, method="GET"):
        response = listNetworkOfferingsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createNetwork(self, command, method="GET"):
        response = createNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNetwork(self, command, method="GET"):
        response = deleteNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworks(self, command, method="GET"):
        response = listNetworksResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def restartNetwork(self, command, method="GET"):
        response = restartNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateNetwork(self, command, method="GET"):
        response = updateNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addNicToVirtualMachine(self, command, method="GET"):
        response = addNicToVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeNicFromVirtualMachine(self, command, method="GET"):
        response = removeNicFromVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateDefaultNicForVirtualMachine(self, command, method="GET"):
        response = updateDefaultNicForVirtualMachineResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addIpToNic(self, command, method="GET"):
        response = addIpToNicResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeIpFromNic(self, command, method="GET"):
        response = removeIpFromNicResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVmNicIp(self, command, method="GET"):
        response = updateVmNicIpResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNics(self, command, method="GET"):
        response = listNicsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def registerSSHKeyPair(self, command, method="GET"):
        response = registerSSHKeyPairResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createSSHKeyPair(self, command, method="GET"):
        response = createSSHKeyPairResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteSSHKeyPair(self, command, method="GET"):
        response = deleteSSHKeyPairResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSSHKeyPairs(self, command, method="GET"):
        response = listSSHKeyPairsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createProject(self, command, method="GET"):
        response = createProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteProject(self, command, method="GET"):
        response = deleteProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateProject(self, command, method="GET"):
        response = updateProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def activateProject(self, command, method="GET"):
        response = activateProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def suspendProject(self, command, method="GET"):
        response = suspendProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listProjects(self, command, method="GET"):
        response = listProjectsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addAccountToProject(self, command, method="GET"):
        response = addAccountToProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAccountFromProject(self, command, method="GET"):
        response = deleteAccountFromProjectResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listProjectAccounts(self, command, method="GET"):
        response = listProjectAccountsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listProjectInvitations(self, command, method="GET"):
        response = listProjectInvitationsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateProjectInvitation(self, command, method="GET"):
        response = updateProjectInvitationResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteProjectInvitation(self, command, method="GET"):
        response = deleteProjectInvitationResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createFirewallRule(self, command, method="GET"):
        response = createFirewallRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteFirewallRule(self, command, method="GET"):
        response = deleteFirewallRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listFirewallRules(self, command, method="GET"):
        response = listFirewallRulesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateFirewallRule(self, command, method="GET"):
        response = updateFirewallRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createEgressFirewallRule(self, command, method="GET"):
        response = createEgressFirewallRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteEgressFirewallRule(self, command, method="GET"):
        response = deleteEgressFirewallRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listEgressFirewallRules(self, command, method="GET"):
        response = listEgressFirewallRulesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateEgressFirewallRule(self, command, method="GET"):
        response = updateEgressFirewallRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateHypervisorCapabilities(self, command, method="GET"):
        response = updateHypervisorCapabilitiesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listHypervisorCapabilities(self, command, method="GET"):
        response = listHypervisorCapabilitiesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createPhysicalNetwork(self, command, method="GET"):
        response = createPhysicalNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deletePhysicalNetwork(self, command, method="GET"):
        response = deletePhysicalNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listPhysicalNetworks(self, command, method="GET"):
        response = listPhysicalNetworksResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updatePhysicalNetwork(self, command, method="GET"):
        response = updatePhysicalNetworkResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listSupportedNetworkServices(self, command, method="GET"):
        response = listSupportedNetworkServicesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addNetworkServiceProvider(self, command, method="GET"):
        response = addNetworkServiceProviderResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNetworkServiceProvider(self, command, method="GET"):
        response = deleteNetworkServiceProviderResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworkServiceProviders(self, command, method="GET"):
        response = listNetworkServiceProvidersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateNetworkServiceProvider(self, command, method="GET"):
        response = updateNetworkServiceProviderResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addTrafficType(self, command, method="GET"):
        response = addTrafficTypeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteTrafficType(self, command, method="GET"):
        response = deleteTrafficTypeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listTrafficTypes(self, command, method="GET"):
        response = listTrafficTypesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateTrafficType(self, command, method="GET"):
        response = updateTrafficTypeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listTrafficTypeImplementors(self, command, method="GET"):
        response = listTrafficTypeImplementorsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createStorageNetworkIpRange(self, command, method="GET"):
        response = createStorageNetworkIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteStorageNetworkIpRange(self, command, method="GET"):
        response = deleteStorageNetworkIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listStorageNetworkIpRange(self, command, method="GET"):
        response = listStorageNetworkIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateStorageNetworkIpRange(self, command, method="GET"):
        response = updateStorageNetworkIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addNetworkDevice(self, command, method="GET"):
        response = addNetworkDeviceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworkDevice(self, command, method="GET"):
        response = listNetworkDeviceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNetworkDevice(self, command, method="GET"):
        response = deleteNetworkDeviceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVPC(self, command, method="GET"):
        response = createVPCResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVPCs(self, command, method="GET"):
        response = listVPCsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVPC(self, command, method="GET"):
        response = deleteVPCResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVPC(self, command, method="GET"):
        response = updateVPCResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def restartVPC(self, command, method="GET"):
        response = restartVPCResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVPCOffering(self, command, method="GET"):
        response = createVPCOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVPCOffering(self, command, method="GET"):
        response = updateVPCOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVPCOffering(self, command, method="GET"):
        response = deleteVPCOfferingResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVPCOfferings(self, command, method="GET"):
        response = listVPCOfferingsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createPrivateGateway(self, command, method="GET"):
        response = createPrivateGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listPrivateGateways(self, command, method="GET"):
        response = listPrivateGatewaysResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deletePrivateGateway(self, command, method="GET"):
        response = deletePrivateGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createNetworkACL(self, command, method="GET"):
        response = createNetworkACLResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateNetworkACLItem(self, command, method="GET"):
        response = updateNetworkACLItemResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNetworkACL(self, command, method="GET"):
        response = deleteNetworkACLResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworkACLs(self, command, method="GET"):
        response = listNetworkACLsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createNetworkACLList(self, command, method="GET"):
        response = createNetworkACLListResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNetworkACLList(self, command, method="GET"):
        response = deleteNetworkACLListResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def replaceNetworkACLList(self, command, method="GET"):
        response = replaceNetworkACLListResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworkACLLists(self, command, method="GET"):
        response = listNetworkACLListsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateNetworkACLList(self, command, method="GET"):
        response = updateNetworkACLListResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createStaticRoute(self, command, method="GET"):
        response = createStaticRouteResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteStaticRoute(self, command, method="GET"):
        response = deleteStaticRouteResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listStaticRoutes(self, command, method="GET"):
        response = listStaticRoutesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createTags(self, command, method="GET"):
        response = createTagsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteTags(self, command, method="GET"):
        response = deleteTagsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listTags(self, command, method="GET"):
        response = listTagsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addResourceDetail(self, command, method="GET"):
        response = addResourceDetailResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeResourceDetail(self, command, method="GET"):
        response = removeResourceDetailResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listResourceDetails(self, command, method="GET"):
        response = listResourceDetailsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVpnCustomerGateway(self, command, method="GET"):
        response = createVpnCustomerGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVpnGateway(self, command, method="GET"):
        response = createVpnGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVpnConnection(self, command, method="GET"):
        response = createVpnConnectionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVpnCustomerGateway(self, command, method="GET"):
        response = deleteVpnCustomerGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVpnGateway(self, command, method="GET"):
        response = deleteVpnGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVpnConnection(self, command, method="GET"):
        response = deleteVpnConnectionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVpnCustomerGateway(self, command, method="GET"):
        response = updateVpnCustomerGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def resetVpnConnection(self, command, method="GET"):
        response = resetVpnConnectionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVpnCustomerGateways(self, command, method="GET"):
        response = listVpnCustomerGatewaysResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVpnGateways(self, command, method="GET"):
        response = listVpnGatewaysResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVpnConnections(self, command, method="GET"):
        response = listVpnConnectionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVpnConnection(self, command, method="GET"):
        response = updateVpnConnectionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVpnGateway(self, command, method="GET"):
        response = updateVpnGatewayResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def generateUsageRecords(self, command, method="GET"):
        response = generateUsageRecordsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listUsageRecords(self, command, method="GET"):
        response = listUsageRecordsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listUsageTypes(self, command, method="GET"):
        response = listUsageTypesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeRawUsageRecords(self, command, method="GET"):
        response = removeRawUsageRecordsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addTrafficMonitor(self, command, method="GET"):
        response = addTrafficMonitorResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteTrafficMonitor(self, command, method="GET"):
        response = deleteTrafficMonitorResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listTrafficMonitors(self, command, method="GET"):
        response = listTrafficMonitorsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addNiciraNvpDevice(self, command, method="GET"):
        response = addNiciraNvpDeviceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteNiciraNvpDevice(self, command, method="GET"):
        response = deleteNiciraNvpDeviceResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNiciraNvpDevices(self, command, method="GET"):
        response = listNiciraNvpDevicesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNiciraNvpDeviceNetworks(self, command, method="GET"):
        response = listNiciraNvpDeviceNetworksResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def addRegion(self, command, method="GET"):
        response = addRegionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateRegion(self, command, method="GET"):
        response = updateRegionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeRegion(self, command, method="GET"):
        response = removeRegionResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listRegions(self, command, method="GET"):
        response = listRegionsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createGlobalLoadBalancerRule(self, command, method="GET"):
        response = createGlobalLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteGlobalLoadBalancerRule(self, command, method="GET"):
        response = deleteGlobalLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateGlobalLoadBalancerRule(self, command, method="GET"):
        response = updateGlobalLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listGlobalLoadBalancerRules(self, command, method="GET"):
        response = listGlobalLoadBalancerRulesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def assignToGlobalLoadBalancerRule(self, command, method="GET"):
        response = assignToGlobalLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def removeFromGlobalLoadBalancerRule(self, command, method="GET"):
        response = removeFromGlobalLoadBalancerRuleResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listVMSnapshot(self, command, method="GET"):
        response = listVMSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createVMSnapshot(self, command, method="GET"):
        response = createVMSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteVMSnapshot(self, command, method="GET"):
        response = deleteVMSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def revertToVMSnapshot(self, command, method="GET"):
        response = revertToVMSnapshotResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createLoadBalancer(self, command, method="GET"):
        response = createLoadBalancerResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listLoadBalancers(self, command, method="GET"):
        response = listLoadBalancersResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteLoadBalancer(self, command, method="GET"):
        response = deleteLoadBalancerResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateLoadBalancer(self, command, method="GET"):
        response = updateLoadBalancerResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def configureInternalLoadBalancerElement(self, command, method="GET"):
        response = configureInternalLoadBalancerElementResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createInternalLoadBalancerElement(self, command, method="GET"):
        response = createInternalLoadBalancerElementResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listInternalLoadBalancerElements(self, command, method="GET"):
        response = listInternalLoadBalancerElementsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createAffinityGroup(self, command, method="GET"):
        response = createAffinityGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deleteAffinityGroup(self, command, method="GET"):
        response = deleteAffinityGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAffinityGroups(self, command, method="GET"):
        response = listAffinityGroupsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def updateVMAffinityGroup(self, command, method="GET"):
        response = updateVMAffinityGroupResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listAffinityGroupTypes(self, command, method="GET"):
        response = listAffinityGroupTypesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def createPortableIpRange(self, command, method="GET"):
        response = createPortableIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def deletePortableIpRange(self, command, method="GET"):
        response = deletePortableIpRangeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listPortableIpRanges(self, command, method="GET"):
        response = listPortableIpRangesResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def stopInternalLoadBalancerVM(self, command, method="GET"):
        response = stopInternalLoadBalancerVMResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def startInternalLoadBalancerVM(self, command, method="GET"):
        response = startInternalLoadBalancerVMResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listInternalLoadBalancerVMs(self, command, method="GET"):
        response = listInternalLoadBalancerVMsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def listNetworkIsolationMethods(self, command, method="GET"):
        response = listNetworkIsolationMethodsResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def getUploadParamsForVolume(self, command, method="GET"):
        response = getUploadParamsForVolumeResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response

    def getUploadParamsForTemplate(self, command, method="GET"):
        response = getUploadParamsForTemplateResponse()
        response = self.connection.marvinRequest(command, response_type=response, method=method)
        return response
