import balder
from balderhub.snmpagent.lib.features.snmp_system_config import SnmpSystemConfig
from balderhub.snmpagent.lib.utils import SnmpPackage
from balderhub.snmpagent.lib.connections import SnmpConnection


@balder.for_vdevice('SnmpAgent', with_connections=SnmpConnection())
class SendSnmpGetRequestCommandFeature(balder.Feature):
    """
    This feature allows to send a snmp GET-REQUEST.
    """

    class SnmpAgent(balder.VDevice):
        """remote agent this feature communicates with"""
        config = SnmpSystemConfig()

    def send(self, oid: str) -> SnmpPackage:
        """
        This method sends a new SNMP-GET REQUEST message

        :param oid: the oid that should be requested

        :return: the snmp package response
        """
        raise NotImplementedError('has to be implemented in subclass')
