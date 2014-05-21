# -*- coding: utf-8 -*-
'''
Config module for pynet devices

'''

import logging
import ast
import re

log = logging.getLogger(__name__)

__virtualname__ = 'config'

__proxyenabled__ = ['pynet']


def __virtual__():
    return __virtualname__
    if 'proxy' in __opts__:
        return __virtualname__
    else:
        return False

def config():
    __opts__['proxyobject'].d.load_config()
    return str(__opts__['proxyobject'].d.config)

