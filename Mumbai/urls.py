from django.urls import path
from Mumbai.views import *
app_name='Mumbai'

urlpatterns=[
    path('Rohit/',Rohit,name='Rohit'),
    path('Suryakumar/',Suryakumar,name='Suryakumar'),
]