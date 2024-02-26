# forms.py
from django import forms
from apis.models import Assessment

class DynamicAssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['data']