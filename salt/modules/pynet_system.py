# -*- coding: utf-8 -*-
'''
System module for pynet devices

'''

import logging
import ast
import re

log = logging.getLogger(__name__)

__virtualname__ = 'system'

__proxyenabled__ = ['pynet']


def __virtual__():
    return __virtualname__
    if 'proxy' in __opts__:
        return __virtualname__
    else:
        return False

def cmd(cmd=''):
    if cmd:
        return str(__opts__['proxyobject'].d.cmd(cmd))

