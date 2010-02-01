# phylo
# Copyright (C) 2010 Phil Christensen
#
# $Id$

import os

from twisted.python import log
from twisted.internet import protocol, reactor

def launch(firefox_path=None, debug_js=False):
	if(not firefox_path):
		firefox_path = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
	
	app_path = os.path.join(os.path.dirname(__file__), 'application.ini')
	
	xul_cmd = [firefox_path, '-app', app_path]
	if(debug_js):
		xul_cmd.append('-jconsole')
	
	reactor.callLater(1, lambda: reactor.spawnProcess(LauncherProtocol(), firefox_path, xul_cmd))

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
