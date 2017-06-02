from setuptools import setup

PACKAGE = 'TracTicketPrinter'
VERSION = '0.1'

setup(name=PACKAGE,
	version=VERSION,
	description="Generate a HTML with tickets ready for printing that can be cut out to use on a Scrum board",
	author="Christofer Karlsson",
	author_email="buxxi@omfilm.net",
	packages=['ticketprinter'],
	entry_points={'trac.plugins': '%s = ticketprinter' % PACKAGE},
	package_data={'ticketprinter' : ['templates/*.html']}
)
