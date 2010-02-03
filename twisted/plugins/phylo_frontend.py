# phylo
# Copyright (C) 2010 Phil Christensen
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

from phylo import xul

class PhyloFrontendServiceMaker(object):
	implements(service.IServiceMaker, IPlugin)
	tapname = "phylo-frontend"
	description = "Run a Phylo front-end server."
	
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
						 ["no-xul", "X", "Don't open XUL interface."],
						]
	
	def makeService(self, config):
		master_service = service.MultiService()
		
		dbapi.debug = config['debug-db']
		
		site_root = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app.handler)
		
		site = server.Site(site_root, logPath=config['accesslog'])
		web_service = internet.TCPServer(config['port'], site, interface=config['interface'])
		web_service.setServiceParent(master_service)
		
		if not(config['no-xul']):
			xul.launch(config['firefox-path'], config['debug-js'])
		
		return master_service

serviceMaker = PhyloFrontendServiceMaker()