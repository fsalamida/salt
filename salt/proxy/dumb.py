# -*- coding: utf-8 -*-
'''
Dumb device for proxy minion.

To see it in action just add this pillar

proxy:
  dumbdevice1:
    proxytype: dumb
  dumbdevice2:
    proxytype: dumb

'''

__proxyenabled__ = ['dumb']


class Proxyconn(object):
    def __init__(self, details):
	pass

    def proxytype(self):
        '''
        Returns the name of this proxy
        '''
        return 'dump'

    def ping(self):
        '''
        Always up
        '''
        return True

