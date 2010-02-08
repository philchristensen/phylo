# phylo
# Copyright (c) 2010 Phil Christensen
#
# $Id: setup.py 1269 2010-02-08 04:27:23Z phil $
#
# See LICENSE for details

import ez_setup
ez_setup.use_setuptools()

import sys, os, os.path

try:
	from twisted import plugin
	from twisted.python.reflect import namedAny
except ImportError, e:
	print >>sys.stderr, "setup.py requires Twisted to create a proper phylo installation. Please install it before continuing."
	sys.exit(1)

from setuptools import setup, find_packages
from setuptools.command import easy_install
import pkg_resources as pkgrsrc

from distutils import log
log.set_threshold(log.INFO)

os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

def autosetup():
	pluginPackages = ['twisted.plugins']
	
	dist_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
	sys.path.insert(0, dist_dir)
	regeneratePluginCache(pluginPackages)
	
	dist = setup(
		name			= "phylo",
		version 		= "0.1",
		packages		= find_packages('src') + ['twisted', 'modu'],
		package_dir		= {'':'src'},
		scripts 		= [],
		app				= ['bootstrap.py'],
		zip_safe		= False,
		
		install_requires 		= ['modu'],
		include_package_data 	= True,
		
		package_data = {
			''			: ['ChangeLog', 'ez_setup.py', 'INSTALL', 'LICENSE', 'README'],
			'twisted'	: ['plugins/modu_web.py'],
			'modu'		: ['sites/phylo_site.py'],
		},
		
		options			= dict(
			py2app			= dict(
				iconfile		= 'webroot/images/phylo.icns',
				plist			= dict(
					CFBundleIdentifier			= 'org.bubblehouse.phylo',
					NSHumanReadableCopyright	= 'Copyright (c) 2010 Phil Christensen',
					LSUIPresentationMode		= 4,
				),
			),
		),
		
		# metadata for upload to PyPI
		author = "Phil Christensen",
		author_email = "phil@bubblehouse.org",
		description = "the phylo media server",
		license = "GPL",
		keywords = "phylo media server home theater",
		#url = "http://phylo.bubblehouse.org",	 # project home page, if any

		# could also include long_description, download_url, classifiers, etc.
	)
	return dist

def pluginModules(moduleNames):
	for moduleName in moduleNames:
		try:
			yield namedAny(moduleName)
		except ImportError:
			pass
		except ValueError, ve:
			if ve.args[0] != 'Empty module name':
				import traceback
				traceback.print_exc()
		except:
			import traceback
			traceback.print_exc()

def regeneratePluginCache(pluginPackages):
	print 'Regenerating plugin cache...'
	for pluginModule in pluginModules(pluginPackages):
		plugin_gen = plugin.getPlugins(plugin.IPlugin, pluginModule)
		try:
			plugin_gen.next()
		except StopIteration, e:
			pass
		except TypeError, e:
			print 'TypeError: %s' % e

if(__name__ == '__main__'):
	__dist__ = autosetup()
