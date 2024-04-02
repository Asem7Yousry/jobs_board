from django.shortcuts import render
from job.models import *

### view to show home page ###
def home(request):

    ### get all categories of system ###
    all_categories = Category.objects.all()

    ### get number of all jobs in data base ###
    number_of_all_jobs = Job.objects.count()

    ### get the latest 6 jobs from database ###
    needed_jobs = Job.objects.order_by('-id')[:6]

    ### all context parameters passed to template ###
    context = {
        'categories' : all_categories,
        'number' : number_of_all_jobs ,
        'jobs' : needed_jobs, 

    }
    return render(request,'index.html',context)

