from django import forms
from .models import Estudiantes, Profesores, Trabajos

class InputForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'
        
    class Meta:
        model = Profesores
        fields = '__all__'
        
    class Meta:
        model = Trabajos
        fields = '__all__'


class SearchForm(forms.Form):
    search_term = forms.CharField(label='Busqueda', max_length=100)
