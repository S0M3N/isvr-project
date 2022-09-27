from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='about'),
    path('contact/', contact, name='contact'),
    path('certificate/<slug:slug>/', cert_check, name='cert_check'),
    path('search', search_cert, name='search_certs'),
]