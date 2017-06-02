from trac.core import implements, Component
from pkg_resources import resource_filename
from trac.mimeview.api import Context, IContentConverter, Mimeview
from trac.web.api import IRequestFilter, RequestDone
from trac.web.chrome import Chrome, ITemplateProvider

class TicketPrinter(Component):
	implements(IContentConverter, ITemplateProvider)

	def get_supported_conversions(self):
		yield ('html', "Ticket printer", 'html', 'trac.ticket.Query', 'text/html', 8)

	def convert_content(self, req, mimetype, content, key):
		content.cols = ['id','summary','description','estimatedhours']
		content = Chrome(self.env).load_template('TicketTemplate.html').generate(tickets=content.execute(req))
		return (unicode(content), 'text/html')

	def get_templates_dirs(self):
		return [resource_filename(__name__, 'templates')]
