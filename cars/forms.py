from django import forms   #importação a classe 'forms'que contem varias funções ja criadas do django sobre o forms.
from cars.models import Brand, Car# Devemos importar o models de brand para que possamos usar o orm capturando todos os modelos cadastrados
#Criamos uma classe que contem todos inputs que queremos que seja cadastrados, esses inputs devem ter relação com a tabela criada em models.
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) #buscando todos os registros da tabela 'Brand', 
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year =  self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            photo = self.cleaned_data['photo'],
        )
        #este save é uma função do models(tabela do banco de dados) que vai salvar as informações acima no banco de dados
        car.save()
        return car
