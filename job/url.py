from django.urls import path
from .views import *

urlpatterns = [
    path('',job_list , name="job_list"),
]


