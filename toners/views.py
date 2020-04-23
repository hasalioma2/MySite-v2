from django.shortcuts import render, redirect
from .models import Toners
from .forms import TonerForm
def index(request):
    toners= Toners.objects.all().order_by('id').reverse()
    form = TonerForm()
    if request.method =="POST":
        form = TonerForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.created_by = request.user
            fs.save()
        return redirect('/')
    context={'toners':toners, 'form':form}
    return render(request, 'index.html', context)