from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

class HtmlToPdf():
    response = None
    def __init__(self, **kwargs):
        html_string = render_to_string(f"{kwargs['arquivo']}.html", {'object_list':kwargs['qs']})
        self.response = HttpResponse(content_type='application/pdf')
        arquivo = f"{kwargs['arquivo']}.pdf"
        self.response['Content-Disposition'] = f'"filename={arquivo}"'
        HTML(string=html_string).write_pdf(self.response)

