# DRAM
# Copyright (C) 2007 Anthology of Recorded Music, Inc.
#
# $Id$

import os, sys

from zope.interface import implements

from twisted.python import usage, log
from twisted.plugin import IPlugin
from twisted.application import internet, service
from twisted.internet import reactor, protocol
from twisted.web import server, wsgi

from modu.web import app
from modu.persist import dbapi

class XULRunnerProtocol(protocol.ProcessProtocol):
	debug = True
	
	def connectionMade(self):
		log.msg('%r connection made' % self)
	
	def outReceived(self, data):
		pass
	
	def errReceived(self, data):
		log.msg('%r stderr: %s' % (self, data))
	
	def processEnded(self, status):
		log.msg('%r process ended' % self)
		reactor.stop()

class PhyloServiceMaker(object):
	implements(service.IServiceMaker, IPlugin)
	tapname = "phylo"
	description = "Run a Phylo media server."
	
	class options(usage.Options):
		"""
		Implement usage parsing for the modu-web plugin.
		"""
		optParameters = [["port", "p", 8888, "Port to use for web server.", int],
						 ['interface', 'i', '', 'Interface to listen on.'],
						 ['accesslog', 'a', None, 'Path to access log.'],
						 ['firefox-path', 'f', None, 'Path to firefox-bin.'],
						]
	
		optFlags =		[["debug-js", "j", "Open JavaScript console."],
						 ["debug-db", "d", "Turn on dbapi debugging."],
						]
	
	def makeService(self, config):
		master_service = service.MultiService()
		
		dbapi.debug = config['debug-db']
		
		site_root = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app.handler)
		
		site = server.Site(site_root, logPath=config['accesslog'])
		web_service = internet.TCPServer(config['port'], site, interface=config['interface'])
		web_service.setServiceParent(master_service)
		
		firefox_path = config['firefox-path']
		if(not firefox_path):
			firefox_path = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
		
		from phylo import xul
		app_path = os.path.join(os.path.dirname(xul.__file__), 'application.ini')
		
		xul_cmd = [firefox_path, '-app', app_path]
		if(config['debug-js']):
			xul_cmd.append('-jconsole')
		
		reactor.callLater(1, lambda: reactor.spawnProcess(XULRunnerProtocol(), firefox_path, xul_cmd))
		
		return master_service

serviceMaker = PhyloServiceMaker()