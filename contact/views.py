from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # send email
            send_mail(
                subject,
                message,
                email,
                ['giovane.zakc@gmail.com'],
                fail_silently=False,
            )
            form.save()
            request.session['contact'] = form.cleaned_data
            return redirect(reverse('contact:contact_success'))

            messages.success(request, f'Form sent with success.')

    else:
        form = ContactForm(user=request.user)
    return render(request, 'contact/contact.html', {'form': form})
    messages.warning(request, f'Please, fill all required fields.')


def contact_success(request):
    return render(request, 'contact/contact_success.html',
                  {'contact': request.session['contact'],
                   'user': request.user})
