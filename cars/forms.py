from django import forms   #importação a classe 'forms'que contem varias funções ja criadas do django sobre o forms.
from cars.models import Car# Devemos importar o models de brand para que possamos usar o orm capturando todos os modelos cadastrados
class CarModelForm(forms.ModelForm):
    class Meta :
        model = Car
        fields = '__all__'
    #validação se o valor do carro for abaixo de 20 mil deve ser informado um erro.
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value','Valor informado abaixo do permitido, o valor deve ser acima de R$20.000')
        return value
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975 :
            self.add_error('factory_year','Carro nao aceito, o ano do carro e menor que o permitido, cadastre carros de 1975 em diante.')
        return factory_year
    
