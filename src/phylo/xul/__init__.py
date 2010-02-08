# phylo
# Copyright (C) 2010 Phil Christensen
#
# $Id$

import os

import pkg_resources as pkg

from twisted.python import log
from twisted.internet import protocol, reactor

def launch():
	open_path = '/usr/bin/open'
	app_bundle = pkg.resource_filename('phylo.xul', 'Phylo.app')
	command = [open_path, '-a', app_bundle, '-W']
	print ' '.join(command)
	reactor.callLater(1, lambda: reactor.spawnProcess(LauncherProtocol(), open_path, command))

class LauncherProtocol(protocol.ProcessProtocol):
	debug = True
	
	def connectionMade(self):
		log.msg('%r connection made' % self)
	
	def outReceived(self, data):
		pass
	
	def errReceived(self, data):
		log.msg('%r stderr: %s' % (self, data))
	
	def processEnded(self, status):
		log.msg('%r process ended' % self)
		if(reactor.running):
			reactor.stop()
