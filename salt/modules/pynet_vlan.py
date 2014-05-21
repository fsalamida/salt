# -*- coding: utf-8 -*-
'''
Interface module for pynet devices

'''

# Import python libraries
import logging
import json

# Set up logging
log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'vlan'

__proxyenabled__ = ['pynet']


def __virtual__():
    return __virtualname__
    if 'proxy' in __opts__:
        return __virtualname__
    else:
        return False

def vlans():
    try:
        ret = json.loads(str(__opts__['proxyobject'].d.vlan))
    except:
        return False
    return ret

def create(vid, **kwargs):
    try:
        vlans = json.loads(str(__opts__['proxyobject'].d.vlan))
    except:
        return False

    vid = str(vid)
    if vid and vid in vlans:
        return False

    log.debug("Creating vlan {0}".format(vid))
    __opts__['proxyobject'].d.vlan.create(vid,**kwargs)

    return True

def delete(vid):
    try:
        vlans = json.loads(str(__opts__['proxyobject'].d.vlan))
    except:
        return False

    vid = str(vid)
    if not vid:
        return False
    if vid not in vlans:
        return False

    log.debug("Deleting vlan {0}".format(vid))
    __opts__['proxyobject'].d.vlan.delete(vid)

    return True

def set_mtu(id, mtu):
    pass

def set_name(id, name):
    pass

def enable(vid):
    try:
        vlans = json.loads(str(__opts__['proxyobject'].d.vlan))
    except:
        return False

    if vid and vid in vlans and 'current state' in vlans[vid] and vlans[vid]['current state'] != 'ACTIVE':
        log.debug("Enabling vlan {0}".format(vid))
        __opts__['proxyobject'].d.vlan.update(vid,state='enable')
        return True
    return False

def disable(vid):
    try:
        vlans = json.loads(str(__opts__['proxyobject'].d.vlan))
    except:
        return False

    if vid and vid in vlans and 'current state' in vlans[vid] and vlans[vid]['current state'] == 'ACTIVE':
        log.debug("Disabling vlan {0}".format(vid))
        __opts__['proxyobject'].d.vlan.update(vid,state='disable')
        return True
    return False

def add_interface(vid, iface=None,tagged='untagged'):
    try:
        ifaces = json.loads(str(__opts__['proxyobject'].d.interface))
        vlans = json.loads(str(__opts__['proxyobject'].d.vlan))
    except:
        return False
    
    vid = str(vid)
    if not vid: 
        return False

    if vid not in vlans:
        return False

    if not iface:
        return False

    if iface not in ifaces:
        return False

    if tagged == 'untagged':
        t = False
    else:
        t = True

    log.debug("Adding interface {1} to vlan {0}".format(vid,iface))
    __opts__['proxyobject'].d.vlan.add_interface(vid,iface,t)
    return True

def remove_interface(vid, iface):
    log.debug("Removing interface {1} from vlan {0}".format(vid,iface))
    __opts__['proxyobject'].d.vlan.delete_interface(vid,iface)
    return True

