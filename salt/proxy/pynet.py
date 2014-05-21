# -*- coding: utf-8 -*-
'''
py-networking device for proxy minion.

proxy:
  switch1:
    proxytype: pynet
    host: <ip address or hostname>
    username: manager
    password: friend

'''
# Import python libs
from __future__ import print_function

import inspect
import logging
import pynetworking
import multiprocessing

log = logging.getLogger(__name__)

__proxyenabled__ = ['pynet']


class Proxyconn(object):
    def __init__(self, details):
        self.d = pynetworking.Device(host=details['host'],username=details['username'],password=details['password'])
        self.d.open()
        log.debug(">>> __init__: process name is {0}".format(multiprocessing.current_process().name))

    def proxytype(self):
        '''
        Returns the name of this proxy
        '''
        return 'pynetworking'

    def ping(self):
        log.debug(">>> ping: process name is {0}".format(multiprocessing.current_process().name))
        return self.d.ping()

    def grains(self):
        log.debug(">>> grains: process name is {0}".format(multiprocessing.current_process().name))
        return self.d.facts

    def shutdown(self, opts):
        try:
            self.d.close()
        except Exception:
            pass
