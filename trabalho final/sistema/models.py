from django.db import models
from stdimage import StdImageField


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Informe o nome')
    celular = models.CharField('Celular', max_length=60, help_text='Informe o celular')
    email = models.CharField('E-mail', max_length=60, help_text='Informe o e-mail')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nome}"


class Corretor(models.Model):
    nome = models.CharField('Nome', max_length=35, help_text='Informe o nome')
    celular = models.CharField('Celular', max_length=35, help_text='Informe o celular')
    email = models.CharField('E-mail', max_length=35, help_text='Informe o e-mail')
    foto = StdImageField('Foto', upload_to='corretores',
                         variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})

    class Meta:
        verbose_name = 'Corretor'
        verbose_name_plural = 'Corretores'

    def __str__(self):
        return self.nome


class Proprietario(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Informe o nome')
    celular = models.CharField('Celular', max_length=60, help_text='Informe o celular')
    email = models.CharField('E-mail', max_length=60, help_text='Informe o e-mail')

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'

    @property
    def imoveis(self):
        return Imovel.objects.filter(proprietario=self)

    def __str__(self):
        return f"{self.nome}"


class Imovel(models.Model):
    codigo = models.CharField('Código', max_length=6, help_text='Informe o código do imóvel')
    endereco = models.CharField('Endereço', max_length=250, help_text='Informe o endereço do imóvel')
    proprietario = models.ForeignKey('sistema.Proprietario', verbose_name='Proprietário', on_delete=models.CASCADE)
    valor_venda = models.DecimalField('Valor de venda', max_digits=5, decimal_places=2, help_text='Informe o valor de venda')
    iptu = models.DecimalField('Valor do IPTU', max_digits=5, decimal_places=2, help_text='Informe o valor do IPTU')
    condominio = models.DecimalField('Valor do condomínio', max_digits=5, decimal_places=2, help_text='Informe o  valor do condomínio')
    area_total = models.DecimalField('Área total', max_digits=5, decimal_places=2, help_text='Informe a área total do imóvel')
    area_privativa = models.DecimalField('Área privativa', max_digits=5, decimal_places=2, help_text='Informe a área privativa do imóvel')
    area_util = models.DecimalField('Área útil', max_digits=5, decimal_places=2, help_text='Informe a área útil do imóvel')
    descricao = models.CharField('Descrição do imóvel', max_length=250, help_text='Descreva o imóvel')
    num_quarto = models.DecimalField('Número de quartos', max_digits=5, decimal_places=2, help_text='Informe a número de quartos')
    num_banheiro = models.DecimalField('Número de banheiros', max_digits=5, decimal_places=2, help_text='Informe a número de banheiros')
    num_garagem = models.DecimalField('Número de vagas de garagem', max_digits=5, decimal_places=2, help_text='Informe a número de vagas de garagem')
    tipo = models.CharField('Tipo', max_length=35, help_text='Informe o tipo de imóvel')
    status = models.CharField('Status', max_length=35, help_text='Informe o status do imóvel')
    comodidade = models.CharField('Comodidades', max_length=250, help_text='Informe as comodidades do imóvel')
    foto = StdImageField('Foto', upload_to='imoveis', variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        return f"{self.codigo}"


class Visita(models.Model):
    imovel = models.ForeignKey('sistema.Imovel', null=True, verbose_name='Imóvel', related_name='imovel_fk', help_text='Selecione o Imóvel', on_delete=models.CASCADE)
    data = models.DateField('data', help_text='Data da visita')
    hora = models.TimeField('hora', help_text='Hora da visita')
    corretor = models.ForeignKey('sistema.Corretor', verbose_name='Corretor', related_name='corretor_fk', help_text='Selecione o Corretor', on_delete=models.CASCADE)
    cliente = models.ForeignKey('sistema.Cliente', verbose_name='Cliente', related_name='cliente_fk', help_text='Selecione o Cliente', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ['data', 'hora']

    def __str__(self):
        return f'{self.data} - {self.hora}'




