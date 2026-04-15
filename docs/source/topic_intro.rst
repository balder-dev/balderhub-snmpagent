Introduction into SNMP
**********************

.. important::
    Please note, that this section is not completed yet.

Simple Network Management Protocol (SNMP) is an Internet Standard that facilitates network administrators to acquire
data of networking devices and control the gadgets remotely. It's broadly utilized in system administration and
surveillance, permitting directors to observe and manage a variety of different apparatuses from one manager device.

This BalderHub package is implemented based on the following RFCs:

* `RFC 1155 <https://datatracker.ietf.org/doc/html/rfc1155>`_
* `RFC 1156 <https://datatracker.ietf.org/doc/html/rfc1156>`_
* `RFC 1157 <https://datatracker.ietf.org/doc/html/rfc1157>`_

Participatory components
========================

There are two main components, that participate inside an SNMP environment.

The SNMP-Agent
--------------

This is the device that provides an SNMP interface.

Often routers, modems, bridges, computers, printers, cameras and so on support SNMP.

The agent is often a own part of the device, that gets the local information and provides it on the SNMP port.

The SNMP-Manager
----------------

This is an application that monitors SNMP information from all SNMP-Agents.

There can be multiple managers inside a network.

Protocol
========

The protocol works with single UDP datagram messages. A protocol entity receives messages at UDP port 161 on the SNMP
agent device (except for Trap messages - these use port 162 on manager).

Message types
-------------

The SNMP protocol supports different message types. The following table shows an overview about them:

+--------------------+----------------------+--------------------------------------------------------------------------+
| Message Type       | Direction            | Description                                                              |
+====================+======================+==========================================================================+
| ``GetRequest``     | ``Manager -> Agent`` | ask for the value of a specific variable or the list of variables        |
+--------------------+----------------------+--------------------------------------------------------------------------+
| ``SetRequest``     | ``Manager -> Agent`` | ask to change the value of a specific variable or the list of variables  |
+--------------------+----------------------+--------------------------------------------------------------------------+
| ``GetNextRequest`` | ``Manager -> Agent`` | message to discover available variables and their values - the agent     |
|                    |                      | returns a response with the value of the next variables                  |
+--------------------+----------------------+--------------------------------------------------------------------------+
| ``Response``       | ``Agent -> Manager`` | answer to a ``GetRequest``, ``SetRequest`` or ``GetNextRequest`` message |
+--------------------+----------------------+--------------------------------------------------------------------------+
| ``Trap``           | ``Agent -> Manager`` | asynchronous message which are not explicit requested - used to notify   |
|                    |                      | the the manager on significant events                                    |
+--------------------+----------------------+--------------------------------------------------------------------------+

Management information base
===========================

SNMP by itself does not define which variables a system should offer. For this, it uses the management information base
(MIB). This definition describes hierarchical organized elements, so called object identifiers (OID), a system could
offer. Depending on the definitions, these OIDs can be read or written by SNMP.