# BalderHub Package `balderhub-snmpagent`

This is a BalderHub package for the `Balder <https://docs.balder.dev/>`_ test framework. It allows 
you to test SNMP agents, without the need of writing own tests. If you are new to Balder check out the
`official documentation <https://docs.balder.dev>`_ first.

## Installation

You can install the latest release with pip:

```
python -m pip install balderhub-snmpagent
```

## Import scenarios

You can activate scenarios by importing them into your project:

```python
# file `scenario_balderhub_snmpagent.py
from balderhub.snmpagent.scenarios.base import ScenarioMibSysDescr, ScenarioMibSysObjectId, ScenarioMibSysUpTime
```

By adding a file, that imports the scenario classes, Balder will collect them automatically (if they are located inside
a file that starts with ``scenario_*.py``)

## Create a setup

If you want to use the shipped PySNMP features, the following setup is ready to use. You only need to provide an 
implementation for the ``SnmpSystemConfig`` feature.

```python
import balder
from .setup_features import MySnmpSystemConfig
from balderhub.snmpagent.lib.features import HasSnmpSystemGroupFeature
from balderhub.snmpagent.lib.setup_features import SendSnmpSetRequestPysnmpFeature, SendSnmpGetRequestPysnmpFeature

class SetupExample(balder.Setup):
    class MySnmpAgent(balder.Device):
        #: this is an autonomous feature which can directly be assigned to your snmp device
        _sys_group = HasSnmpSystemGroupFeature()
        #: your custom configuration feature (that holds you specific settings)
        config = MySnmpSystemConfig()

    @balder.connect(with_device="MySnmpAgent", over_connection=balder.Connection())
    class ThisPc(balder.Device):
        #: this an already implemented pysnmp feature that allows to send SNMP GET packages
        snmp_get = SendSnmpGetRequestPysnmpFeature(SnmpAgent="MySnmpAgent")
        #: this an already implemented pysnmp feature that allows to send SNMP SET packages
        snmp_set = SendSnmpSetRequestPysnmpFeature(SnmpAgent="MySnmpAgent")
```

Checkout [the example section of the documentation](https://hub.balder.dev/projects/snmpagent/en/latest/examples.html) 
for more details.

# Check out the documentation

If you need more information, 
[checkout the ``balderhub-snmpagent`` documentation](https://hub.balder.dev/projects/snmpagent).


# License

This BalderHub package is free and Open-Source

Copyright (c) 2022 Max Stahlschmidt and others

Distributed under the terms of the MIT license