from django import forms
from .models import Sample

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['name', 'sample_type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sample_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
