from django import forms   #importação a classe 'forms'que contem varias funções ja criadas do django sobre o forms.
from cars.models import Brand # Devemos importar o models de brand para que possamos usar o orm capturando todos os modelos cadastrados
#Criamos uma classe que contem todos inputs que queremos que seja cadastrados, esses inputs devem ter relação com a tabela criada em models.
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) #buscando todos os registros da tabela 'Brand', 
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
