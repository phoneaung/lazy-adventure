from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Candidate, Comment
from .forms import AddCandidateForm, AddCommentForm

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
            candidate.last_modified_by = request.user
            candidate.save()

            messages.success(request, "Candidate has successfully created!")

            return redirect('/dashboard/')
    else:
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
            # let users remove their current image or resume 
            if 'image-clear' in request.POST:
                candidate.image.delete(save=False)
                candidate.image = None

            # if the image is empty, assign the default image
            instance = form.save(commit=False)
            if not instance.image:
                instance.image = 'default_image.jpg'
            instance.save()
            
            if 'resume-clear' in request.POST:
                candidate.resume.delete(save=False)
                candidate.resume = None
        
            candidate.last_modified_by = request.user
            form.save()

            messages.success(request, 'The changes were saved!')
            return redirect('candidates_list')
    else:
        
        form = AddCandidateForm(instance=candidate)

    return render(request, 'candidate/edit_candidate.html', {
        'form': form,
        'candidate': candidate,
    })


# delete candidate
@login_required
def delete_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    candidate.delete()

    messages.success(request, 'The candidate has been deleted!')
    return redirect('candidates_list')


# add comments
@login_required
def comment(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)

    if request.method == 'POST':
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = form.cleaned_data['comment']
            comment = Comment.objects.create(candidate=candidate, members=request.user, comment=comment)
            comment.save()

            messages.success(request, 'You have added a comment!')

        return redirect('candidate_details', pk=pk)
    
    else:
        form = AddCommentForm()

    return redirect('candidate_details', pk=pk)