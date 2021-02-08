from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cliente, Corretor, Proprietario, Imovel, Visita

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email')
    search_fields = ('email',)
    list_filter = ('nome',)

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email', 'foto')
    search_fields = ('email',)
    list_filter = ('nome',)
    readonly_fields = ["fotografia"]

    def fotografia(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.foto.url,
            width=obj.foto.width,
            height=obj.foto.height,
        ))




@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email', 'get_imoveis')
    search_fields = ('email',)
    list_filter = ('nome',)

    def get_imoveis(self, obj):
        return ','.join([imovel.codigo for imovel in Imovel.objects.filter(proprietario=obj.id)])

    get_imoveis.short_description= 'Imóveis'


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'endereco', 'proprietario', 'valor_venda', 'iptu', 'condominio', 'area_total', 'area_privativa', 'area_util', 'descricao', 'num_quarto', 'num_banheiro', 'num_garagem', 'tipo', 'status', 'comodidade', 'foto')
    search_fields = ('endereco',)
    list_filter = ('codigo',)
    readonly_fields = ['fotografia']

    def fotografia(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url = obj.foto.url,
            width = obj.foto.width,
            height = obj.foto.height,
        ))

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('imovel','corretor', 'cliente', 'data', 'hora')
    search_fields = ('data',)
    list_filter = ('corretor', 'cliente')





