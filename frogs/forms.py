from django import forms
from .models import FrogAquarium, Frog

class FrogAquariumForm(forms.ModelForm):
    class Meta:
        model = FrogAquarium
        fields = ['aquarium_size', 'aquarium_price']
        widgets = {
            'aquarium_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '20x40'}),
            'aquarium_price': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

class FrogForm(forms.ModelForm):
    class Meta:
        model = Frog
        fields = ['frog_type', 'aquarium', 'price']
        widgets = {
            'frog_type': forms.Select(attrs={'class': 'form-select'}),
            'aquarium': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Авто-цена'})
        }

        def clean_proce(self):
            price = self.cleaned_data.get('price')
            if price is not None and price < 0:
                raise forms.ValidationError('Лягушка не может стоить отрицательных значений')
            return price