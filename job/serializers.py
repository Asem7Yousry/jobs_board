from rest_framework import serializers
from .models import Job

### create class for job serializer ###
class JobSerializer(serializers.ModelSerializer):
    ### choose model we serialize it ###
    class Meta:
        model = Job
        fields = "__all__"



