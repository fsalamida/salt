# -*- coding: utf-8 -*-
'''
Grains for dumb device.
'''
__proxyenabled__ = ['dumb']

__virtualname__ = 'dumb'


def __virtual__():
    if 'proxy' not in __opts__:
        return False
    else:
        return __virtualname__


def os_family():
    return {'os_family': 'dumbos'}


