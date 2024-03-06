from django import forms
from .models import Bids

class BidsForm(forms.ModelForm):
    class Meta:
        model = Bids
        fields = '__all__'

        widgets = {
            'bid_opening_time': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            'bid_closing_time': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        }
