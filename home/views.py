from typing import Any
from django.shortcuts import render
from job.models import *
from django.views.generic import TemplateView

### view to show home page ###
# def home(request):

#     ### get all categories of system ###
#     all_categories = Category.objects.all()

#     ### get number of all jobs in data base ###
#     number_of_all_jobs = Job.objects.count()

#     ### get the latest 6 jobs from database ###
#     needed_jobs = Job.objects.order_by('-id')[:6]

#     ### all context parameters passed to template ###
#     context = {
#         'categories' : all_categories,
#         'number' : number_of_all_jobs ,
#         'jobs' : needed_jobs, 

#     }
#     return render(request,'index.html',context)

## logic view to show home page ##
class HomePage(TemplateView):
    ### pass the template name to be rendered ###
    template_name = 'index.html'

    ## pass some context data ##
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        ### get all categories of system ###
        context['categories'] = Category.objects.all()
        ## get lattest 6 jobs in system data base ##
        context['jobs'] = Job.objects.order_by('-id')[:6] 
        ## get count number of all jobs ##
        context['number'] = Job.objects.count()

        return context