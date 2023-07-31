from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
	name=models.CharField('Name', max_length=30, null=True, blank=True)
	email=models.EmailField('Email', null=False, blank=True)
	phone_number=models.CharField('Phone', null=False, blank=True, default='no contact', max_length=15)
	message=models.TextField('Message', blank=True)
	date=models.DateTimeField('Date', default=datetime.now())

	def __str__(self):
		return f'{self.name} on {self.phone_number}'