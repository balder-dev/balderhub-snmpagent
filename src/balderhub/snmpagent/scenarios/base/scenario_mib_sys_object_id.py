import balder
from balderhub.snmpagent.lib import features
from balderhub.snmpagent.lib.utils import SnmpPackage
from balderhub.snmpagent.lib.connections import SnmpConnection


class ScenarioMibSysObjectId(balder.Scenario):
    """
    This scenario is used for testing the system group defined in the RFC1156.
    """
    OID = '1.3.6.1.2.1.1.2.0'

    VALUE_FOR_ILLEGAL_SET = '1.3.6.1.4.1.123.123.123.123'

    @balder.connect('SnmpManager', over_connection=SnmpConnection())
    class SnmpAgent(balder.Device):
        """the remote snmp agent device"""
        #: autonomous feature of type :class:`HasSnmpSystemGroupFeature` to define that this device is able to handle
        #: SNMP messages of group `system`
        _snmp_sys = features.HasSnmpSystemGroupFeature()
        #: general configuration from type :class:`SnmpSystemConfig`
        snmp_system_config = features.SnmpSystemConfig()

    class SnmpManager(balder.Device):
        """the snmp manager device"""
        #: feature of type :class:`SendSnmpGetRequestCommandFeature` which allows sending SNMP GET REQUEST messages
        snmp_send_get = features.SendSnmpGetRequestCommandFeature(SnmpAgent="SnmpAgent")
        #: feature of type :class:`SendSnmpSetRequestCommandFeature` which allows sending SNMP SET REQUEST messages
        snmp_send_set = features.SendSnmpSetRequestCommandFeature(SnmpAgent="SnmpAgent")

    def _verify_response(self, snmp_response: SnmpPackage):
        assert snmp_response.error_status == 0, \
            f'received an error status of `{snmp_response.error_status}` in GET-RESPONSE'
        assert snmp_response.get_value_of(oid=self.OID) == self.SnmpAgent.snmp_system_config.sys_object_id, \
            f'the value (=`{snmp_response.get_value_of(oid=self.OID)}`) for `sysObjectId` is not the expected one ' \
            f'(=`{self.SnmpAgent.snmp_system_config.sys_object_id}`)'

    def test_get_sys_object_id(self):
        """
        This test tries to request the `sysObjectId` object.
        """
        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        self._verify_response(get_response)

    def test_set_sys_object_id(self):
        """
        This test tries to set the `sysObjectId` object, while it secures that it is not possible.
        """
        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        self._verify_response(get_response)

        assert get_response.get_value_of(oid=self.OID) != self.VALUE_FOR_ILLEGAL_SET, \
            "the previous value and the value that should be used for the illegal set are the same - can not " \
            "continue, because validation is not possible"

        set_response = self.SnmpManager.snmp_send_set.send(self.OID, self.VALUE_FOR_ILLEGAL_SET)
        assert set_response.error_status == 17, \
            f"did not receive error status 17 (received `{set_response.error_status}`) while executing a illegal set " \
            f"request (which is not allowed, because value is read-only)"

        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        self._verify_response(get_response)
