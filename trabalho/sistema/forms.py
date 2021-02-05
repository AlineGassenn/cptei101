from django import forms
from sistema.models import Imovel, Corretor, Cliente, Proprietario, Visita

class VisitaListForm(forms.Form):

    corretores = forms.ModelChoiceField(label='Corretor: ', widget=forms.Select(attrs={'class':'select is-fullwidth'}),
                                      queryset=Corretor.objects.all(), required=False)

    imoveis = forms.ModelChoiceField(label='Imóvel: ', widget=forms.Select(attrs={'class': 'select is-fullwidth'}),
                                      queryset=Imovel.objects.all(), required=False)


class CorretorModelForm(forms.ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type':'text', 'placeholder': 'Digite o nome do corretor'}),
            'celular': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o celular do corretor'}),
            'email': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do corretor'}),
            'foto': forms.FileInput(attrs={'class': 'input', 'type':'file'}),

        }

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do cliente'}),
            'celular': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o celular do cliente'}),
            'email': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do cliente'}),
        }

class ProprietarioModelForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do proprietário'}),
            'celular': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o celular do proprietário'}),
            'email': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do proprietário'}),
        }

class ImovelModelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(
                attrs={'class': 'input', 'type':'text', 'placeholder': 'Digite o código do imóvel'}),
            'endereco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o endereço do imóvel'}),
            'proprietario': forms.Select(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Selecione o proprietario do imóvel'}),
            'valor_venda': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o valor de venda do imóvel'}),
            'iptu': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o valor do IPTU do imóvel'}),
            'condominio': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o valor do codomínio do imóvel'}),
            'area_total': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a área total do imóvel'}),
            'area_privativa': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a área privativa do imóvel'}),
            'area_util': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a área útil do imóvel'}),
            'descricao': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Descreva o imóvel'}),
            'num_quarto': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o número de quartos do imóvel'}),
            'num_banheiro': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o número de banheiros do imóvel'}),
            'num_garagem': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o número de vagas de garagem do imóvel'}),
            'tipo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Informe o tipo do imóvel'}),
            'status': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Informe o status do imóvel'}),
            'comodidade': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Informe as comodidades do imóvel'}),
            'foto': forms.FileInput(attrs={'class': 'input', 'type':'file'}),
        }

class VisitaModelForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        widgets = {
            'imovel': forms.Select(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Informe o imóvel'}),
            'data': forms.DateInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Informe a data da visita'}),
            'hora': forms.TimeInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Informe a hora da visita'}),
            'corretor': forms.Select(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Selecione o corretor'}),
            'cliente': forms.Select(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Selecione o cliente'}),
        }