from setuptools import setup, find_packages
setup(
	name			= "Phylo",
	version 		= "0.1",
	packages		= find_packages(),
	scripts 		= [],
	app				= ['bootstrap.py'],

	# Project uses reStructuredText, so ensure that the docutils get
	# installed or upgraded on the target machine
	install_requires 		= ['twisted'],
	include_package_data 	= True,
	
	package_data	= dict(
		twisted			= ['plugins/phylo_frontend.py'],
	),
	
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