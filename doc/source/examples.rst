Examples
********

This section shows different simple examples how you can integrate these tests.

Configure feature
=================

The feature :class:`balderhub.snmpagent.lib.features.SnmpSystemConfig` has to be overwritten to configure your setup
device:

.. code-block:: python

    from balderhub.snmpagent.lib.features import SnmpSystemConfig


    class MySnmpSystemConfig(SnmpSystemConfig):
        @property
        def host(self) -> str:
            """the ip address of the SNMP device"""
            return "192.168.0.123"

        @property
        def read_community(self) -> str:
            """snmp community (for reading) that is configured in the SNMP device"""
            return "public"

        @property
        def write_community(self) -> str:
            """snmp community (for writing) that is configured in the SNMP device"""
            return "private"

        @property
        def sys_descr(self) -> str:
            """the expected value that should be returned as `sysDescr` for this device"""
            return "My nice device"

        @property
        def sys_object_id(self) -> str:
            """the expected value that should be returned as `sysObjectId` for this device"""
            return "1.3.6.1.4.1.1234.12.3.4.1"


Use shipped PySNMP features
===========================

This BalderHub package is shipped with some already implemented features, that can directly be used by your setup. For
this just add the following features to your setup:

.. code-block:: python

    from .setup_features import MySnmpSystemConfig
    from balderhub.snmpagent.lib.features import HasSnmpSystemGroupFeature
    from balderhub.snmpagent.lib.setup_features import SendSnmpSetRequestPysnmpFeature, SendSnmpGetRequestPysnmpFeature

    class SetupExample(balder.Setup):
        class MySnmpAgent(balder.Device):
            #: this is an autonomous feature which can directly be assigned to your snmp device
            _sys_group = HasSnmpSystemGroupFeature()
            #: your configuration feature which was defined before
            config = MySnmpSystemConfig()

        @balder.connect(with_device="MySnmpAgent", over_connection=balder.Connection())
        class ThisPc(balder.Device):
            #: this an already implemented pysnmp feature that allows to send SNMP GET packages
            snmp_get = SendSnmpGetRequestPysnmpFeature(SnmpAgent="MySnmpAgent")
            #: this an already implemented pysnmp feature that allows to send SNMP SET packages
            snmp_set = SendSnmpSetRequestPysnmpFeature(SnmpAgent="MySnmpAgent")

.. note::
    Note that you have to provide a VDevice mapping to a device that implements the
    :class:`balderhub.snmpagent.lib.features.SnmpSystemConfig`.

Create own custom features
==========================

Of course you can also implement the GET/SET features by yourself. For this, just overwrite the scenario-level features
:class:`balderhub.snmpagent.lib.features.SendSnmpGetRequestCommandFeature` and the
:class:`balderhub.snmpagent.lib.features.SendSnmpSetRequestCommandFeature`.

