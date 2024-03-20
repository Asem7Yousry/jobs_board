from django.shortcuts import render , redirect
from django.urls import reverse
# from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from .forms import *

#### function to show all jobs in database #####
def job_list(request):
    ### get all jobs objects from database ###
    all_jobs = Job.objects.all()
    ## specify number of jobs per page 
    paginator = Paginator(all_jobs, 5)
    ## get page number from request (GET method)
    page_numnber = request.GET.get('page')
    ## jobs in page number 
    jobs_of_page = paginator.get_page(page_numnber)
    ### passed contant to render page 
    contant = {"jobs":jobs_of_page,"all_jobs":all_jobs}
    ### render the ui of jobs with specific needed jobs 
    return render(request,'jobs.html',contant)

#### function to show the details of each job ####
def job_details(request , slug):
    ### get job by its slug ####
    requested_job = Job.objects.get(slug = slug)
    ### check if request method is post 
    if request.method == "POST":
        ### get form with requested data ###
        form = Apply_form(request.POST,request.FILES)
        #### check validation of requested data ####
        if form.is_valid():
            ### save a temporary copy requested data of form in table of application in data base ####
            myform = form.save(commit=False)
            ### save a job field in applictaion ### 
            myform.job = requested_job
            #### save all fields of appliction model ####
            myform.save()
            ### redirect to job list page ###
            return redirect("job_list")
    ### if request method is get ###
    else:
        #### empty form ####
        form = Apply_form()
    ### render job deatails page
    return render(request, 'job_details.html',{'job':requested_job , 'form':form})

#### function for post a new job #####
def post_job(request):
    #### check if method of form is post 
    if request.method == "POST":
        ### make instance request in apply form
        form = Post_job(request.POST)
        ### check validation of requested data form 
        if form.is_valid():
            ### save requested data form in db 
            form.save()
            ### redirect to job list page after saving
            return redirect(reverse("job_list"))
    ##### if request method is get #####
    else:
        form = Post_job()
    return render(request,"post_job.html",{"form":form})

