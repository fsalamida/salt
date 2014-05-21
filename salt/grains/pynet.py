# -*- coding: utf-8 -*-
'''
Generate pynetworking proxy minion grains
'''
__proxyenabled__ = ['pynet']

__virtualname__ = 'pynet'


def __virtual__():
    if 'proxy' not in __opts__:
        return False
    else:
        return __virtualname__


def os_data():
    return __opts__['proxyobject'].grains()
