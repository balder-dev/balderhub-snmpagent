from typing import Union, List
from dataclasses import dataclass


@dataclass
class VarBind:
    """
    A single var bind object which is part of the most :class:`SnmpPackage` objects
    """
    name: str
    value: Union[str, int, None]


@dataclass
class SnmpPackage:
    """
    Base snmp package class which describes a single SNMP package in this balderhub environment
    """
    version: str
    community: str
    error_status: int
    error_index: int
    variable_bindings: List[VarBind]

    def get_value_of(self, oid) -> Union[str, int, None]:
        """
        This method returns the value for the given OID that is contained in the internal `variable_bindings` list.

        :param oid: the oid of the variable that should be returned

        :return: the value of the given oid
        """
        for cur_var_bind in self.variable_bindings:
            if cur_var_bind.name == oid:
                return cur_var_bind.value
        raise KeyError(f'the oid `{oid}` does not exist in the internal variable-bindings')
