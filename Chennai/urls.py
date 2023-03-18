from django.urls import path
from Chennai.views import *
app_name='Chennai'

urlpatterns=[
    path('Dhoni/',Dhoni,name='Dhoni'),
    path('Suresh/',Suresh,name='Suresh'),
]