import django_filters
from .models import Job

### class for job filter ###
class JobFilter(django_filters.FilterSet):
    ## cascade on title and decsription field to search with key words ##
    title = django_filters.CharFilter(lookup_expr = 'icontains')
    description = django_filters.CharFilter(lookup_expr = 'icontains')

    ## specify model we need ##
    class Meta:
        model = Job
        fields = ['title','job_type','description','category']
