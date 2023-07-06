from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from candidate.models import Candidate

@login_required
def dashboard(request):
    candidates = Candidate.objects.filter(is_active=True).order_by('-created_at')[0:5]
    
    return render(request, 'dashboard/dashboard.html', {
        'candidates': candidates
    })
