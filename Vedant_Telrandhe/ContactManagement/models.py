from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import validate_email


class Contact(models.Model):
    id=models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100, unique=True)
    emailId=models.EmailField(unique=True)
    notes = models.CharField(max_length=255, default='No notes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        # Validate the email field
        validate_email(self.emailId)

    def __str__(self):
        return self.fullname
    

