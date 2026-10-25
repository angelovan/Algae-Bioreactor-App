from django import forms
from .models import ExperimentLog

class ExperimentLogForm(forms.ModelForm):
    class Meta:
        model = ExperimentLog
        fields = '__all__'
        widgets = {
            'bioreactor': forms.Select(attrs={'class': 'form-control'}),
            'date_recorded': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'measured_ph': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 8.2'}),
            'measured_temp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 28.5'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Student observations:'})
        }

    def clean_measured_temp(self):
        temp = self.cleaned_data.get('measured_temp')
        if temp < 10 or temp > 30:
            raise forms.ValidationError("Temperature must be between 10°C and 30°C.")
        return temp