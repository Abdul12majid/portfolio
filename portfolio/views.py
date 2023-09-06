from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.views.decorators.http import require_http_methods

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
	return render(request, "index.html", {})

def about(request):
	return render(request, 'index.html', {})

def my_resume(request):
	return render(request, 'resume.html', {})


def contact_me(request):
	form=ContactForm(request.POST)
	
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			your_name=form.cleaned_data['name']
			
			your_email=form.cleaned_data['email']
			receiver=[your_email]
			subject='Hello'
			link='https://twitter.com/_Adeiza_'
			message=f'Good day {your_name}. Please click any of the link below to get in touch.\n {link}'
			db=Contact.objects.filter(email=form.cleaned_data['email']).exists()

			sender=settings.EMAIL_HOST_USER
			
			if not db:
				send_mail(subject, message, sender, receiver, fail_silently=True)
				messages.success(request, (f'Thank you for reaching out {your_name}. An email has been sent to you, please follow the instruction.'))
				
				form.save()
				return redirect("contact-me")
			else:

				messages.success(request, (f' Your initial message was receieved, please await reply.'))
				return render(request, "contact.html", {'form':form})
		
	return render(request, 'contact.html', {'form':form})

def services(request):
	return render(request, 'services.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def project(request):
	return render(request, 'projects.html', {})

def my_cv(request):
	return render(request, 'my_cv.html', {})
