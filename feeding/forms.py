from django import forms
from .models import NutrientFeed


class NutrientFeedForm(forms.ModelForm):
    class Meta:
        model = NutrientFeed
        fields = ['bioreactor', 'completed_date', 'notes']
        widgets = {
            'completed_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }