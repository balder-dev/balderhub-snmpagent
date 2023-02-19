import balder
from balder import connections


@balder.insert_into_tree([connections.UdpIPv4Connection, connections.UdpIPv6Connection])
class SnmpConnection(balder.Connection):
    """
    SNMP connection which is based on UDP (IPv4 or IPv6)
    """
