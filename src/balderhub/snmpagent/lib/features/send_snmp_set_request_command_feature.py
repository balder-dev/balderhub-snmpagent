from typing import Union
import balder
from balderhub.snmpagent.lib.features.snmp_system_config import SnmpSystemConfig
from balderhub.snmpagent.lib.connections import SnmpConnection


@balder.for_vdevice('SnmpAgent', with_connections=SnmpConnection())
class SendSnmpSetRequestCommandFeature(balder.Feature):
    """
    This feature allows to send a snmp SET-REQUEST.
    """

    class SnmpAgent(balder.VDevice):
        """remote agent this feature communicates with"""
        config = SnmpSystemConfig()

    def send(self, oid: str, value: Union[str, int, None]):
        """
        This method allows to send a message to the remote snmp agent.

        :param oid:

        :param value:
        """
        raise NotImplementedError('has to be implemented in subclass')
