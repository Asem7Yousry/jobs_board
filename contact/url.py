from django.urls import path , include
from .views import *

urlpatterns = [

    path('', send_message , name='contact_us'),
    
]