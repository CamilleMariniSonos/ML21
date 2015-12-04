from django.shortcuts import render
from django.views.generic import ListView
from motorapp.models import Dataset

def welcome(request):
    context = {'main_info': 'oh yeah'}
    return render(request, 'motorapp/welcome.html', context)

class DatasetList(ListView):
    template_name = 'motorapp/list_dataset.html'
    model = Dataset
    context_object_name = 'dataset'


