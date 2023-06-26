from django import forms

from .models import Candidate

class AddCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'description', 'email', 'phone', 'image', 'resume',)