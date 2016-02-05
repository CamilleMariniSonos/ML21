from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from motorapp.models import Dataset, Problem
#from motorapp.management.commands import upload_dataset
from .forms import UploadFileForm
import task

def welcome(request):
    context = {'main_info': 'oh yeah'}
    return render(request, 'motorapp/welcome.html', context)

class DatasetList(ListView):
    template_name = 'motorapp/list_dataset.html'
    model = Dataset
    context_object_name = 'dataset'

def upload_dataset(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if not Dataset.objects.filter(description=form.cleaned_data['description']):
                newdataset = Dataset(description=form.cleaned_data['description'], \
                                                raw_data=request.FILES['file'])
                newdataset.save()
                newproblem = Problem(dataset=newdataset,
                                     pb_type=form.cleaned_data['pb_type'])
                newproblem.save()
                context['success'] = 'So far, so good! Your dataset has been uploaded!'
                score = task.train_test(newdataset.raw_data.path,
                                        newproblem.pb_type)
                context['score'] = score
            else:
                context['error'] = 'Oups, your dataset has not been uploaded, since \
                                    this description already exists, change it!'
    else:
        form = UploadFileForm()
    context['form'] = form
    return render_to_response('motorapp/upload_dataset.html', context,
                              context_instance=RequestContext(request))

def problem_definition(request):
    context = {}
    return render_to_response('motorapp/problem_definition.html', context,
                              ontext_instance=RequestContext(request))
