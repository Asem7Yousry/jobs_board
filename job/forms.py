from django import forms
from .models import Job , Application

################## all forms for job app #################

#### from for post a new job ####
# class Post_job(forms.ModelForm):
#     ### specify model used ####
#     class Meta:
#         ### the model that form will deal with it ###
#         model = Job
#         ### take all fields of model ###
#         fields = "__all__"
#         ### excute 3 fields from model to be in form ###
#         exclude = ('published_date','image','slug')

#### form for apply for job ####
class Apply_form(forms.ModelForm):
    #### specify the needed model ####
    class Meta:
        model = Application
        ### take all fields in model ###
        fields = "__all__"
        ### excute job and date ###
        exclude = ['job', 'date']
    