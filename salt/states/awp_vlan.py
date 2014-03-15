# -*- coding: utf-8 -*-
'''
Vlan management for Alliedware plus switches
============================================

.. versionadded:: develop

This state is used to manage vlan database in Allied Telesis switches with Alliedware+ OS.

.. code-block:: yaml

    admin:
      vlan:
        - managed
        - id: 10

'''

# Import python libs
import logging

# Import salt libs
import salt.utils

log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'vlan'

__proxyenabled__ = ['awp']


def __virtual__():
    if 'proxy' in __opts__:
        return __virtualname__
    else:
        return False


def managed(name, id=1):
    '''
    Manage vlan

    name
        vlan name
    id
        vlan id is an integer between 1 and 4095
    '''
    # Just in case someone decides to enter a numeric description
    name = str(name)

    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': 'Vlan {0} already exists and has id {1}'.format(name,id)}

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = ('Vlan {0} created with id {1}'.format(name,id))
        return ret

    return ret

