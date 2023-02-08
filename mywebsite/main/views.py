from django.shortcuts import render

from mywebsite.main.models import Estudiantes, Profesores, Trabajos
from .forms import InputForm, SearchForm

def input_data(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InputForm()
    return render(request, 'main/input.html', {'form': form})
    
def search_data(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            class1_results = Estudiantes.objects.filter(name__contains=search_term)
            class2_results = Profesores.objects.filter(title__contains=search_term)
            class3_results = Trabajos.objects.filter(item__contains=search_term)
            return render(request, 'main/search_results.html', {'Estudiantes': class1_results, 'Profesores': class2_results, 'Trabajos': class3_results})
    else:
        form = SearchForm()
    return render(request, 'main/search.html', {'form': form})
