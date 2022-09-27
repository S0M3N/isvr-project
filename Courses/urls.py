from django.urls import path
from .views import *

urlpatterns=[
    path('', courses, name='contact'),
    path('apply/', apply, name='home'),
    path('<slug:slug>/', course, name='course'),
]