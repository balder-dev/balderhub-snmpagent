from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, getCmd
from balderhub.snmpagent.lib.features.send_snmp_get_request_command_feature import SendSnmpGetRequestCommandFeature
from balderhub.snmpagent.lib.utils import SnmpPackage, get_var_binds_from_pysnmp_response


class SendSnmpGetRequestPysnmpFeature(SendSnmpGetRequestCommandFeature):
    """
    This feature provides a basic implementation of the :class:`SendSnmpGetRequestCommandFeature` with the pysnmp
    package.

    .. note::
        Please note, this feature implementation uses the SNMP version v2c!
    """

    def send(self, oid: str) -> SnmpPackage:
        iterator = getCmd(SnmpEngine(), CommunityData(self.SnmpAgent.config.read_community),
                          UdpTransportTarget((self.SnmpAgent.config.host, self.SnmpAgent.config.snmp_port)),
                          ContextData(), ObjectType(ObjectIdentity(oid)))
        _, error_status, error_index, var_binds = next(iterator)

        return SnmpPackage(
            version="v2c", community=self.SnmpAgent.config.read_community, error_status=int(error_status),
            error_index=int(error_index), variable_bindings=get_var_binds_from_pysnmp_response(var_binds))
