from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('my_resume', views.my_resume, name='my-resume'),
    path('contact', views.contact_me, name='contact-me'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('projects', views.project, name='projects'),
    path('my_cv', views.my_cv, name='my-cv'),
    path('mail', views.mail, name='mail'),
    
]
