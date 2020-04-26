from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from .models import Toners
from .forms import TonerForm,BranchForm


def Index(request):
    url_parameter = request.GET.get("q")
    if url_parameter:
        toners=Toners.objects.filter(branch__name__icontains = url_parameter)
    else:
        toners= Toners.objects.all().order_by('id').reverse()
    
    form = TonerForm()
    form2= BranchForm()
    if request.method =="POST":
        form = TonerForm(request.POST)
        form2 = BranchForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.created_by = request.user
            fs.save()
        if form2.is_valid():
            fs= form2.save()
        return redirect('/')
    
    context={'toners':toners, 'form':form, 'form2':form2}

    return render(request, 'index.html', context)
