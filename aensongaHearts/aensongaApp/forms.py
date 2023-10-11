from django import forms
from aensongaApp.models import Donation

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['email', 'amount']