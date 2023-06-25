from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def candidate(request):
    return render(request, 'candidate/candidate.html')
