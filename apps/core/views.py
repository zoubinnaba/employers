from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

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


def detail(request, employer_id):
    employer = get_object_or_404(Employer, pk=employer_id)
    return render(request, "core/detail.html", {"employer": employer})