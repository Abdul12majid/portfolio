from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model=Contact
		fields=('name', 'email', 'phone_number', 'message')
		widgets={

		    'name':forms.TextInput(attrs={'class':'form-control', 'required':'True', 'placeholder':'Name *', 'type':'text', 'name':'your-name'}),
		    'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Valid Email *', 'required':'True', 'type':'email', 'email':'your-email'}),
		    'phone_number':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Contact no *', 'required':'True', 'type':'number', 'name':'your-number'}),
		    'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message *', 'type':'text', 'required':'True', 'name':'your-message'}),
		}
		labels={

		    'name':'',
		    'email':'',
		    'phone_number':'',
		    'message':'',
		    
		}
		error_messages={
		    'name':{
		        'unique':("Contact with this name already exists, pick another."),
		        
		    },
		}