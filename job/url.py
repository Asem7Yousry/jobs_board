from django.urls import path
from .views import *
from .api import job_list_api , job_details_api

urlpatterns = [
    path('',job_list , name="job_list"),
    # path('',JobList.as_view() , name="job_list"),
    # path('<str:slug>',job_details , name="job_details"),
    path('<str:slug>',JobDetail.as_view() , name="job_details"),
    path('apply/<int:pk>',ApplyJob.as_view() , name="apply_job"),
    # path('post_job/',post_job , name="post_job"),
    path('post_job/',PostJobForm.as_view() , name="post_job"),
    ### api links ###

    ## function based views links ##
    path('api/jobs/',job_list_api , name="job_list_api"),
    path('api/jobs/<str:slug>',job_details_api , name="job_details_api"),

    

]


