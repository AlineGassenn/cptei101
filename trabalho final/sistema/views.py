from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cliente, Corretor, Proprietario, Imovel, Visita
from django.db.models import Q
from .forms import VisitaListForm, CorretorModelForm, ClienteModelForm, ProprietarioModelForm, ImovelModelForm, VisitaModelForm
from .utils import HtmlToPdf



class IndexView(TemplateView):
    template_name = 'index.html'

class ClienteView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    queryset = Cliente.objects.all()

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs= super(ClienteView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='clientes_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClienteView, self).get(*args, **kwargs)

class CorretorView(ListView):
    model = Corretor
    template_name = 'corretores.html'
    queryset = Corretor.objects.all()

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs= super(CorretorView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='corretores_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(CorretorView, self).get(*args, **kwargs)

class ProprietarioView(ListView):
    model = Proprietario
    template_name = 'proprietarios.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs= super(ProprietarioView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='proprietarios_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ProprietarioView, self).get(*args, **kwargs)

class ImovelView(ListView):
    model = Imovel
    template_name = 'imoveis.html'
    queryset = Imovel.objects.all()

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs= super(ImovelView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(codigo__icontains=buscar)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='imoveis_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ImovelView, self).get(*args, **kwargs)


class VisitaView(ListView):
    model = Visita
    template_name = 'visitas.html'
    queryset = Visita.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VisitaView, self).get_context_data(**kwargs)

        if self.request.GET:
            form = VisitaListForm(self.request.GET)
        else:
            form = VisitaListForm()

        context['form'] = form
        return context

    def get_queryset(self):
        qs = super(VisitaView, self).get_queryset()

        if self.request.GET:
            form = VisitaListForm(self.request.GET)
            if form.is_valid():
                corretor = form.cleaned_data.get('corretores')
                imovel = form.cleaned_data.get('imoveis')

                if corretor:
                    qs = qs.filter(corretor=corretor)
                if imovel:
                    qs = qs.filter(imovel=imovel)
        return qs

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='visitas_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(VisitaView, self).get(*args, **kwargs)

class CorretoresAddView(CreateView):
    form_class = CorretorModelForm
    model = Corretor
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')

class CorretoresUpDateView(UpdateView):
    form_class = CorretorModelForm
    model = Corretor
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')

class CorretoresDeleteView(DeleteView):
    form_class = CorretorModelForm
    model = Corretor
    template_name = 'corretor_apagar.html'
    success_url = reverse_lazy('corretores')

class ClientesAddView(CreateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClientesUpDateView(UpdateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClientesDeleteView(DeleteView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')

class ProprietariosAddView(CreateView):
    form_class = ProprietarioModelForm
    model = Proprietario
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')

class ProprietariosUpDateView(UpdateView):
    form_class = ProprietarioModelForm
    model = Proprietario
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')

class ProprietariosDeleteView(DeleteView):
    form_class = ProprietarioModelForm
    model = Proprietario
    template_name = 'proprietario_apagar.html'
    success_url = reverse_lazy('proprietarios')

class ImoveisAddView(CreateView):
    form_class = ImovelModelForm
    model = Imovel
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')

class ImoveisUpDateView(UpdateView):
    form_class = ImovelModelForm
    model = Imovel
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')

class ImoveisDeleteView(DeleteView):
    form_class = ImovelModelForm
    model = Imovel
    template_name = 'imovel_apagar.html'
    success_url = reverse_lazy('imoveis')

class VisitasAddView(CreateView):
    form_class = VisitaModelForm
    model = Visita
    template_name = 'visita_form.html'
    success_url = reverse_lazy('visitas')

class VisitasUpDateView(UpdateView):
    form_class = VisitaModelForm
    model = Visita
    template_name = 'visita_form.html'
    success_url = reverse_lazy('visitas')

class VisitasDeleteView(DeleteView):
    form_class = VisitaModelForm
    model = Visita
    template_name = 'visita_apagar.html'
    success_url = reverse_lazy('visitas')