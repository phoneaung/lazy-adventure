from django import forms

from .models import Candidate

class AddCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'description', 'status', 'email', 'phone', 'image', 'resume',)

        # only a sigle file can be selected at a time
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
            'resume': forms.ClearableFileInput(attrs={'multiple': False}),
        }