from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Candidate
from .forms import AddCandidateForm

# show all candidates
@login_required
def candidates_list(request):
    candidates = Candidate.objects.filter(is_active=True)
    
    return render(request, 'candidate/candidate.html', {
        'candidates': candidates,
    })

# create new candidate 
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