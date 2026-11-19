from django import forms
from motorcycles.models import Motorcycle


class MotorcycleModelForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = '__all__'


    def clean_value(self): # validação do campo
        value = self.cleaned_data.get('value')
        if value < 19000:
            self.add_error('value','Valor mínimo de uma moto custom dever ser a partir de R$19.000')
        return value


    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1950:
            self.add_error('factory_year', 'Não é possivel cadastrar motos custom fabricados antes de 1950')
        return factory_year

    