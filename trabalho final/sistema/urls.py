from django.urls import path
from .views import IndexView, ClienteView, ProprietarioView, ImovelView, VisitaView, CorretorView, \
    CorretoresAddView, CorretoresUpDateView, CorretoresDeleteView, ClientesAddView, ClientesUpDateView, \
    ClientesDeleteView, ProprietariosAddView, ProprietariosUpDateView, ProprietariosDeleteView, ImoveisAddView, \
    ImoveisUpDateView, ImoveisDeleteView, VisitasAddView, VisitasUpDateView, VisitasDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clientes', ClienteView.as_view(), name='clientes'),
    path('corretores', CorretorView.as_view(), name='corretores'),
    path('proprietarios', ProprietarioView.as_view(), name='proprietarios'),
    path('imoveis', ImovelView.as_view(), name='imoveis'),
    path('visitas', VisitaView.as_view(), name='visitas'),
    path('corretor/adicionar/', CorretoresAddView.as_view(), name='corretor_adicionar'),
    path('<int:pk>/corretor/editar/', CorretoresUpDateView.as_view(), name='corretor_editar'),
    path('<int:pk>/corretor/apagar/', CorretoresDeleteView.as_view(), name='corretor_apagar'),
    path('cliente/adicionar/', ClientesAddView.as_view(), name='cliente_adicionar'),
    path('<int:pk>/cliente/editar/', ClientesUpDateView.as_view(), name='cliente_editar'),
    path('<int:pk>/cliente/apagar/', ClientesDeleteView.as_view(), name='cliente_apagar'),
    path('proprietario/adicionar/', ProprietariosAddView.as_view(), name='proprietario_adicionar'),
    path('<int:pk>/proprietario/editar/', ProprietariosUpDateView.as_view(), name='proprietario_editar'),
    path('<int:pk>/proprietario/apagar/', ProprietariosDeleteView.as_view(), name='proprietario_apagar'),
    path('imovel/adicionar/', ImoveisAddView.as_view(), name='imovel_adicionar'),
    path('<int:pk>/imovel/editar/',  ImoveisUpDateView.as_view(), name='imovel_editar'),
    path('<int:pk>/imovel/apagar/',  ImoveisDeleteView.as_view(), name='imovel_apagar'),
    path('visita/adicionar/', VisitasAddView.as_view(), name='visita_adicionar'),
    path('<int:pk>/visita/editar/', VisitasUpDateView.as_view(), name='visita_editar'),
    path('<int:pk>/visita/apagar/', VisitasDeleteView.as_view(), name='visita_apagar'),
]