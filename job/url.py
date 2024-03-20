from django.urls import path
from .views import *

urlpatterns = [
    path('',job_list , name="job_list"),
    path('<str:slug>',job_details , name="job_details"),
    path('post_job/',post_job , name="post_job"),

]


