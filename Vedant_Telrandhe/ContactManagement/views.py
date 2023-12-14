from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    contacts=Contact.objects.all()

    return render(request,'index.html',{'contacts':contacts})