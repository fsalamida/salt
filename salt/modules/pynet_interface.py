# -*- coding: utf-8 -*-
'''
Interface module for pynet devices

'''

import logging
import re
import json

log = logging.getLogger(__name__)

__virtualname__ = 'interface'

__proxyenabled__ = ['pynet']


def __virtual__():
    return __virtualname__
    if 'proxy' in __opts__:
        return __virtualname__
    else:
        return False

def interfaces(iface=None):
    try:
        ret = json.loads(str(__opts__['proxyobject'].d.interface))
    except:
        return False
    if iface:
        for name in ret:
           if name == iface:
               ret = {name:ret[name]}
               break
        else:
           return False
    return ret

def enable(iface):
    try:
        ifaces = json.loads(str(__opts__['proxyobject'].d.interface))
    except:
        return False

    if iface and iface in ifaces and 'enable' in ifaces[iface] and not ifaces[iface]['enable']:
        log.debug("Enabling interface {0}".format(iface))
        __opts__['proxyobject'].d.interface.update(iface,enable=True)
        return True
   
    return False

def disable(iface):
    try:
        ifaces = json.loads(str(__opts__['proxyobject'].d.interface))
    except:
        return False

    if iface and iface in ifaces and 'enable' in ifaces[iface] and ifaces[iface]['enable']:
        log.debug("Disabling interface {0}".format(iface))
        __opts__['proxyobject'].d.interface.update(iface,enable=False)
        return True
   
    return False

def set_description(iface, desc=None):
    if not desc:
        return False

    try:
        ifaces = json.loads(str(__opts__['proxyobject'].d.interface))
    except:
        return False

    if iface and iface in ifaces:
        log.debug("setting '{1}' for interface {0}".format(iface, desc))
        __opts__['proxyobject'].d.interface.update(iface, description=str(desc))
        return True
    return False


