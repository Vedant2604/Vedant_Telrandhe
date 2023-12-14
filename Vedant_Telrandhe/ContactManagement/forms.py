from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'emailId','notes']
        error_messages = {
            'fullname': {
                'unique': "This name is already in use.",
            },
            'emailId': {
                'unique': "This email is already in use.",
                'invalid': "Enter a valid email address.",
            },
            
        }