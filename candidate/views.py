from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Candidate
from .forms import AddCandidateForm

# show all candidates and let users search candidates
@login_required
def candidates_list(request):
    candidates = Candidate.objects.filter(is_active=True)
    query = request.GET.get('query')

    if query:
        candidates = candidates.filter(name__icontains=query)

    return render(request, 'candidate/candidate_list.html', {
        'candidates': candidates,
        'query': query,
    })


# detail page of candidate
@login_required
def candidate_details(request, pk):
    candidate = get_object_or_404(Candidate, is_active=True, pk=pk)

    return render(request, 'candidate/candidate_details.html', {
        'candidate': candidate
    })


# create new candidate 
@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = AddCandidateForm(request.POST, request.FILES)

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


# edit candidates
@login_required
def edit_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)

    if request.method == 'POST':
        form = AddCandidateForm(request.POST, request.FILES, instance=candidate)

        if form.is_valid():
            candidate.last_modified_by = request.user
            form.save()

            messages.success(request, 'The changes were saved!')
            return redirect('/candidates_list/')
    else:
        form = AddCandidateForm(instance=candidate)

    return render(request, 'candidate/edit_candidate.html', {
        'form': form,
        'candidate': candidate,
    })
