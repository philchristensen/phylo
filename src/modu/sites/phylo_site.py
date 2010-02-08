# phylo
# Copyright (C) 2010 phylo
#
# $Id$
#

import os.path

from zope.interface import classProvides

from twisted import plugin

from modu import assets
from modu.web import app, static
from modu.editable import resource
from modu.editable.datatypes import fck

from phylo.resource import index

class Site(object):
	classProvides(plugin.IPlugin, app.ISite)
	
	def initialize(self, application):
		application.base_domain = 'localhost'
		application.db_url = 'sqlite3://localhost/phylodb'
		application.admin_calc_found_rows = False
		application.use_db_locks = False
		application.template_dir = 'phylo', 'template'
		
		import phylo
		compiled_template_root = os.path.abspath(os.path.join(os.path.dirname(phylo.__file__), '../var'))
		if(os.path.exists(compiled_template_root)):
			application.compiled_template_root = compiled_template_root
		
		application.activate('/assets', static.FileResource, os.path.dirname(assets.__file__))
		
		import phylo.itemdefs
		application.activate('/admin', resource.AdminResource, default_path='admin/listing/page', itemdef_module=phylo.itemdefs)
		
		application.activate('/fck', fck.FCKEditorResource)
		application.activate('/', index.Resource)
