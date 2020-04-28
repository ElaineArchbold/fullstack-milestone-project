from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages

# Create your views here.


def home(request):
    """A view that displays the index page"""
    return render(request, "home.html")


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            query = request.POST.get('query', '')

            template = get_template('contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'query': query,
            }
            content = template.render(context)
            messages.error(request, "Thank you for your message. We will be in touch soon!")
            email = EmailMessage("New contact form submission", content, "Alio Prints" + '', ['alioprints@gmail.com'], headers={'Reply-To': email})
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {'form': form_class,})
