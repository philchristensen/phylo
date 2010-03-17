# phylo
# Copyright (C) 2010 Phil Christensen
#
# $Id: phylo_frontend.py 1275 2010-02-08 18:15:45Z phil $

import os, sys

from zope.interface import implements

from twisted.python import usage, log
from twisted.plugin import IPlugin
from twisted.application import internet, service
from twisted.internet import reactor, protocol
from twisted.web import server

from modu import app
from modu.persist import dbapi

class PhyloBackendServiceMaker(object):
	implements(service.IServiceMaker, IPlugin)
	tapname = "phylo-backend"
	description = "Run a Phylo back-end server."
	
	class options(usage.Options):
		"""
		Implement usage parsing for the phylo-backend plugin.
		"""
		optParameters = [["port", "p", 8887, "Port to use for web server.", int],
						 ['interface', 'i', '', 'Interface to listen on.'],
						 ['accesslog', 'a', None, 'Path to access log.'],
						]
	
		optFlags =		[["debug-db", "d", "Turn on dbapi debugging."],
						]
	
	def makeService(self, config):
		master_service = service.MultiService()
		
		dbapi.debug = config['debug-db']
		
		site_root = wsgi.WSGIResource(reactor, reactor.getThreadPool(), app.handler)
		
		site = server.Site(site_root, logPath=config['accesslog'])
		web_service = internet.TCPServer(config['port'], site, interface=config['interface'])
		web_service.setServiceParent(master_service)
		
		return master_service

serviceMaker = PhyloBackServiceMaker()