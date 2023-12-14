from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    contacts=Contact.objects.all()

    return render(request,'index.html',{'contacts':contacts})

def addContact(request, id=None):
    if id:
        contact = Contact.objects.get(pk=id)
        form = ContactForm(request.POST or None, instance=contact)
    else:
        form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                return redirect('index')  
            except ValidationError as e:
                form.add_error(None, e)
    return render(request, 'addContact.html', {'form': form})

def deleteContact(request,id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect(reverse('index'))  # Redirect to your contact list view
    return render(request, 'confirm_delete.html', {'contact': contact})

def updateContact(request, id):
    # Retrieve the existing contact or return a 404 error if it doesn't exist
    contact = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            try:
                form.save()
                return redirect('index') 
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = ContactForm(instance=contact)

    return render(request, 'updateContact.html', {'form': form, 'contact': contact})

def viewDetails(request, id):
    contact = get_object_or_404(Contact, pk=id)
    return render(request, 'viewDetails.html', {'contact': contact})