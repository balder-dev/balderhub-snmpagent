import time
import math
import balder
from balderhub.snmpagent.lib import features
from balderhub.snmpagent.lib.utils import SnmpPackage
from balderhub.snmpagent.lib.connections import SnmpConnection


class ScenarioMibSysUpTime(balder.Scenario):
    """
    This scenario is used for testing the system group defined in the RFC1156.
    """
    OID = '1.3.6.1.2.1.1.3.0'

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
        sys_up_time = snmp_response.get_value_of(oid=self.OID)
        assert isinstance(sys_up_time, int), f'the value (=`{sys_up_time}`) for `sysUpTime` is not from type int'
        assert sys_up_time > 0, f'the value (=`{sys_up_time}`) for `sysUpTime` is not bigger than 0'

    def test_get_sys_up_time(self):
        """
        This test tries to request the `sysUpTime` object.
        """
        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        self._verify_response(get_response)

    def test_get_sys_up_time_changed_check(self):
        """
        This test tries to request the `sysUpTime` object.

        .. note::
            This test is not as accurate to validate the exact correct value of sysUpTime. This test is created for
            validating if the sysUpTime increase in an expected way. It doesn't ensure any accuracy.
        """
        start_time_before_send = time.perf_counter()
        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        start_time_after_send = time.perf_counter()
        self._verify_response(get_response)
        sys_up_time_first = get_response.get_value_of(self.OID)

        time.sleep(0.5)

        end_time_before_send = time.perf_counter()
        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        end_time_after_send = time.perf_counter()
        self._verify_response(get_response)
        sys_up_time_second = get_response.get_value_of(self.OID)

        time_tick_diff = sys_up_time_second - sys_up_time_first
        min_allowed_time_ticks = math.floor((end_time_before_send - start_time_after_send) * 100)
        max_allowed_time_ticks = math.ceil((end_time_after_send - start_time_before_send) * 100)
        assert min_allowed_time_ticks < time_tick_diff < max_allowed_time_ticks,  \
            f"sysUpTime delta time is not in allowed area (min: {min_allowed_time_ticks} | max: " \
            f"{max_allowed_time_ticks}) - is {time_tick_diff}"

    def test_set_sys_up_time(self):
        """
        This test tries to set the `sysUpTime` object, while it secures that it is not possible.
        """
        add_on_time = 10000

        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        self._verify_response(get_response)
        sys_up_time_before = get_response.get_value_of(oid=self.OID)

        set_response = self.SnmpManager.snmp_send_set.send(self.OID, sys_up_time_before + add_on_time)
        assert set_response.error_status == 17, \
            f"did not receive error status 17 (received `{set_response.error_status}`) while executing an illegal " \
            f"set request (which is not allowed, because value is read-only)"

        get_response = self.SnmpManager.snmp_send_get.send(self.OID)
        self._verify_response(get_response)

        sys_up_time_after = get_response.get_value_of(oid=self.OID)

        assert sys_up_time_before <= sys_up_time_after < sys_up_time_before + add_on_time, \
            f'the value (=`{sys_up_time_after}`) for `sysUpTime` is not in the expected area between the value ' \
            f'before (`{sys_up_time_before}`) and the failed set value (`{sys_up_time_before + add_on_time}`)'
