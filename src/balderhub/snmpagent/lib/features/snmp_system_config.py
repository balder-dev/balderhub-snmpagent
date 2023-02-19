import balder


class SnmpSystemConfig(balder.Feature):
    """
    This feature provides the general snmp configuration for a snmp agent device
    """

    @property
    def host(self) -> str:
        """
        :return: the host domain or ip address of the snmp agent
        """
        raise NotImplementedError('has to be implemented in subclass')

    @property
    def snmp_port(self) -> int:
        """
        :return: the snmp port of the snmp agent
        """
        return 161

    @property
    def read_community(self) -> str:
        """
        :return: the community for read access to this snmp agent
        """
        raise NotImplementedError('has to be implemented in subclass')

    @property
    def write_community(self) -> str:
        """
        :return: the community for write access to this snmp agent
        """
        raise NotImplementedError('has to be implemented in subclass')

    @property
    def sys_descr(self) -> str:
        """
        :return: the expected ``sysDescr`` for this snmp agent
        """
        raise NotImplementedError('has to be implemented in subclass')

    @property
    def sys_object_id(self) -> str:
        """
        :return: the expected ``sysObjectId`` for this snmp agent
        """
        raise NotImplementedError('has to be implemented in subclass')
