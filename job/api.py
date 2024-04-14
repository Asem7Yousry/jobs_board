from .serializers import JobSerializer
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view

### function api view to list all jobs in json formate ###
@api_view(['GET'])
def job_list_api(request):
    ### get all jobs objects from data base ###
    all_jobs = Job.objects.all()
    ### serialize all jobs ###
    serialized_data = JobSerializer(all_jobs , many= True).data
    ### responce serialized data to template ###
    return Response({'data':serialized_data})

#### function to get job details by its slug ####
@api_view(['GET'])
def job_details_api(request,slug):
    ### get required job ###
    job = Job.objects.get(slug= slug)
    ### serialize data ###
    serialized_job = JobSerializer(job).data
    ### return response ###
    return Response({'data':serialized_job})

