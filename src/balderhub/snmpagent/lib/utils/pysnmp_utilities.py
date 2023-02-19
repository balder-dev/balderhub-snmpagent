from typing import List
from pysnmp.hlapi import TimeTicks, OctetString, ObjectIdentity
from .snmp_package import VarBind


def get_var_binds_from_pysnmp_response(response) -> List[VarBind]:
    """
    Helper function that extracts the :class:`VarBind` objects from a pysnmp command

    :param response: the var-bind object which is returned from pysnmp

    :return: a list with all balderhub :class:`VarBind` objects
    """
    variable_bindings = []
    for cur_identity, cur_object in response:
        if isinstance(cur_object, TimeTicks):
            cur_object = int(cur_object)
        elif isinstance(cur_object, (OctetString, ObjectIdentity)):
            cur_object = str(cur_object)
        else:
            raise TypeError(f'the type `{cur_object.__class__}` of received data is not supported by this balder '
                            f'feature')

        variable_bindings.append(VarBind(str(cur_identity), cur_object))
    return variable_bindings
