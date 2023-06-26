from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Candidate
from .forms import AddCandidateForm

@login_required
def candidate(request):
    return render(request, 'candidate/candidate.html')

@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = AddCandidateForm(request.POST)

        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.created_by = request.user
            candidate.save()

            messages.success(request, "Candidate has successfully created!")

            return redirect('/dashboard/')

    form = AddCandidateForm()

    return render(request, 'candidate/add_candidate.html', {
        'form': form
    })