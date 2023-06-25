from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Candidate
from .forms import AddCandidateForm

@login_required
def candidate(request):
    return render(request, 'candidate/candidate.html')

@login_required
def add_candidate(request):
    form = AddCandidateForm()

    return render(request, 'candidate/add_candidate.html', {
        'form': form
    })