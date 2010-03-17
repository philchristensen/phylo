# phylo
# Copyright (C) 2010 Phil Christensen
#
# $Id$

from txjsonrpc.web import jsonrpc

class APIResource(jsonrpc.JSONRPC):
	def __init__(self):
		jsonrpc.JSONRPC.__init__(self)
		jsonrpc.addIntrospection(self)

