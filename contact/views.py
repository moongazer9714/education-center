from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_obj(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    context = {
        "form": form
    }
    return render(request, 'contact/contact.html', context)
