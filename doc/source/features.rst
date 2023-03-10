Features
********


This section describes all features that are shipped with this package. Specially take a look at the
`PySNMP setup features <PySNMP setup Features>`, which are ready-to-use setup features, that can directly be used in
your setup.

Scenario Features
=================

SnmpManagerDevice
-----------------

.. autoclass:: balderhub.snmpagent.lib.features.HasSnmpSystemGroupFeature
    :members:

.. autoclass:: balderhub.snmpagent.lib.features.SnmpSystemConfig
    :members:

SnmpAgentDevices
----------------

.. autoclass:: balderhub.snmpagent.lib.features.SendSnmpGetRequestCommandFeature
    :members:

.. autoclass:: balderhub.snmpagent.lib.features.SendSnmpSetRequestCommandFeature
    :members:


PySNMP setup Features
=====================

SnmpAgentDevices
----------------

This section holds features that can directly be used in your setup.

.. autoclass:: balderhub.snmpagent.lib.setup_features.SendSnmpGetRequestPysnmpFeature
    :members:

.. autoclass:: balderhub.snmpagent.lib.setup_features.SendSnmpSetRequestPysnmpFeature
    :members:

