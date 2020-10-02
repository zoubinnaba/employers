from django.shortcuts import render, redirect

from .models import Employer
from .forms import EmployerForm

def frontpage(request):
    employers = Employer.objects.all()[:5]
    return render(request, "core/frontpage.html", {"employers": employers})


def createEmployer(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('frontpage')
    else:
        form = EmployerForm()
    return render(request, "core/create.html", {"form": form})