from typing import Any
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse
# from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import JobFilter
## for class based views ##
from django.views.generic import FormView , ListView , CreateView , DetailView

#### function to show all jobs in database #####
def job_list(request):
    ### get all jobs objects from database ###
    all_jobs = Job.objects.all().order_by('-published_date')
    ## count of all jobs ##
    count = all_jobs.count()
    ## filter in  all jobs ##
    myfilter = JobFilter(request.GET,queryset= all_jobs )
    ## override on alljobs variable ##
    all_jobs = myfilter.qs
    ## specify number of jobs per page 
    paginator = Paginator(all_jobs, 10)
    ## get page number from request (GET method)
    page_numnber = request.GET.get('page')
    ## jobs in page number 
    jobs_of_page = paginator.get_page(page_numnber)
    ### passed contant to render page 
    contant = {"jobs":jobs_of_page,"all_jobs":all_jobs ,'filter':myfilter , 'count':count}
    ### render the ui of jobs with specific needed jobs 
    return render(request,'job/job_list.html',contant)

#### class view to list all jobs in database #####
# class JobList(ListView):
#     model = Job
#     context_object_name = 'jobs'
#     ordering = ['-published_date']
#     paginate_by = 5

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # Apply any filters here
#         myfilter = JobFilter(self.request.GET, queryset=queryset)
#         return myfilter.qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         ## pass cont of all jobs to context ##
#         context['count'] = Job.objects.count()
#         # Include pagination-related context data
#         context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
#         return context
    
#### function to show the details of each job ####
# @login_required
# def job_details(request , slug):
#     ### get job by its slug ####
#     requested_job = Job.objects.get(slug = slug)
#     ### check if request method is post 
#     if request.method == "POST":
#         ### get form with requested data ###
#         form = Apply_form(request.POST,request.FILES)
#         #### check validation of requested data ####
#         if form.is_valid():
#             ### save a temporary copy requested data of form in table of application in data base ####
#             myform = form.save(commit=False)
#             ### save a job field in applictaion ### 
#             myform.job = requested_job
#             #### save all fields of appliction model ####
#             myform.save()
#             ### redirect to job list page ###
#             return redirect("job_list")
#     ### if request method is get ###
#     else:
#         #### empty form ####
#         form = Apply_form()
#     ### render job deatails page
#     return render(request, 'job/job_details.html',{'job':requested_job , 'form':form})

#### view to show each job indetails ####
class JobDetail(DetailView, FormView):
    model = Job
    template_name = 'job/job_details.html'
    context_object_name = 'job'
    form_class = Apply_form
    success_url = '/jobs'

### view to apply on the job ###
class ApplyJob(DetailView , LoginRequiredMixin ,FormView):
    model = Job
    form_class = Apply_form
    context_object_name = 'job'
    success_url = '/jobs'
    template_name = 'job/apply_job.html'

    ## if application form is valid ##
    def form_valid(self ,form):
        form = form.save(commit=False)
        form.job = self.get_object()
        form.save()
        return super().form_valid(form)
    
    ## if not valid ##
    def form_invalid(self, form):
        return redirect('apply_job')


############################# POST JOB in different ways ###################################

#### function for post a new job #####
# @login_required
# def post_job(request):
#     #### check if method of form is post 
#     if request.method == "POST":
#         ### make instance request in apply form
#         form = Post_job(request.POST)
#         ### check validation of requested data form 
#         if form.is_valid():
#             ### save requested data form in db 
#             form.save()
#             ### redirect to job list page after saving
#             return redirect(reverse("job_list"))
#     ##### if request method is get #####
#     else:
#         form = Post_job()
#     return render(request,"job/post_job.html",{"form":form})

#### class view to post view #####
# class PostJobForm(LoginRequiredMixin , FormView):
#     form_class = Post_job
#     template_name = 'job/post_job.html' ## template to be render ##
#     ## url to redirect after successfull post job process ##
#     success_url = '/jobs'

#     ## check validation ##
#     def form_valid(self, form):
#         ## save new job in models data base ##
#         form.save()
#         return super().form_valid(form)

#     ## if request post form not valid ##
#     def form_invalid(self, form):
#         ## redirect to the same form ##
#         return redirect('post_job')
#         # return super().form_invalid(form)

#### class view to post view #####
class PostJobForm(LoginRequiredMixin , CreateView):
    model = Job
    fields = ['title','job_type','description','Vacancy','salary','category','experience_years']
    success_url = '/jobs'   
    template_name = 'job/post_job.html'
    