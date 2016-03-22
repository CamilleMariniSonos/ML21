from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from motorapp.models import Dataset, Problem
from .forms import UploadFileForm, ProblemForm
import task


def welcome(request):
    context = {'main_info': 'oh yeah'}
    return render(request, 'motorapp/welcome.html', context)


class DatasetList(ListView):
    template_name = 'motorapp/list_dataset.html'
    model = Dataset
    context_object_name = 'dataset'


@login_required
def upload_dataset(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if not Dataset.objects.filter(description=form.
                                          cleaned_data['description']):
                newdataset = Dataset(description=form.
                                     cleaned_data['description'],
                                     raw_data=request.FILES['file'],
                                     user=request.user)
                newdataset.save()
                return redirect("motorapp:run")
            else:
                context['error'] = 'Oups, your dataset has not been uploaded, \
                                    since this description already exists, \
                                    change it!'
    else:
        form = UploadFileForm()
    context['form'] = form
    return render_to_response('motorapp/upload_dataset.html', context,
                              context_instance=RequestContext(request))


@login_required
def run_analysis(request):
    context = {}
    # context['list_dataset'] = Dataset.object.filter(user=request.user)
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            newproblem = Problem(dataset=form.cleaned_data['dataset'],
                                 pb_type=form.cleaned_data['pb_type'])
            newproblem.save()
            context['success'] = 'Oh yeah'
            score = task.train_test(newproblem.dataset.raw_data.path,
                                    newproblem.pb_type)
            print score
            context['score'] = score
        else:
            context['error'] = 'problem in problem'
    else:
        form = ProblemForm()
    context['form'] = form
    return render_to_response('motorapp/run_analysis.html', context,
                              context_instance=RequestContext(request))
