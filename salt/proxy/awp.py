# -*- coding: utf-8 -*-
'''
Alliedware plus OS device for proxy minion.

proxy:
  switch1:
    proxytype: awp

'''

__proxyenabled__ = ['awp']


class Proxyconn(object):
    def __init__(self, details):
	pass

    def proxytype(self):
        '''
        Returns the name of this proxy
        '''
        return 'awp'

    def ping(self):
        '''
        Always up
        '''
        return True

