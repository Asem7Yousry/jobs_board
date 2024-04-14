from django.urls import path
from .views import *
from .api import job_list_api , job_details_api

urlpatterns = [
    path('',job_list , name="job_list"),
    path('<str:slug>',job_details , name="job_details"),
    path('post_job/',post_job , name="post_job"),
    ### api links ###

    ## function based views links ##
    path('api/jobs/',job_list_api , name="job_list_api"),
    path('api/jobs/<str:slug>',job_details_api , name="job_details_api"),

    

]


