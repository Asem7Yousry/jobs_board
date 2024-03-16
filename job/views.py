from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator


def job_list(request):
    ### get all jobs objects from database ###
    all_jobs = Job.objects.all()
    #### get number of jobs in data base 
    number_of_jobs = len(all_jobs)
    ## specify number of jobs per page 
    paginator = Paginator(all_jobs, 10)
    ## get page number from request (GET method)
    page_numnber = request.GET.get('page')
    ## jobs in page number 
    jobs_of_page = paginator.get_page(page_numnber)
    ### passed contant to render page 
    contant = {"jobs":jobs_of_page,"number":number_of_jobs}
    ### render the ui of jobs with specific needed jobs 
    return render(request,'jobs.html',contant)

