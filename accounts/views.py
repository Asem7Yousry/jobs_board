from typing import Any
from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth import authenticate , login
from .models import Profile
from django.contrib import messages
from django.views.generic import TemplateView

#### sign up function ####
def signup(request):
    ### check the request method ###
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #### check the validation of data of form ####
        if form.is_valid():
            ## save data form in user model ##
            form.save()
            ### get username and passwoerd ####
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            ### check authentication of user data  ###
            user = authenticate(username= username , password= password)
            ### make user login ###
            login(request,user)
            ### go to profile pages ###
            return redirect('/')
    ### if request metod is get ###
    else:
        form = SignUpForm()
    return render(request,'registration\sign_up.html',{'form':form})

#### view of show profile data ####
# def show_profile(request):
#     ### get profile object of user in request ###
#     profile = Profile.objects.get(user= request.user)
#     ## render profile page ###
#     return render(request,'accounts\profile.html',{'profile':profile})

#### class view of show profile data ####
class Profile_View(TemplateView):
    template_name = 'accounts\profile.html'
    
    def get_context_data(self ,**kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user = self.request.user)
        return context

#### view to edit profile data ###
def edit_profile(request):
    ### check if request method is post ###
    if request.method == 'POST':
        #### add forms of user and profile fields with requested data ####
        user_form = UserEditForm(request.POST , instance= request.user)
        profile_form = EditProfileForm(request.POST, request.FILES ,instance= request.user.profile)
        ### check validation of data requested ###
        if user_form.is_valid() and profile_form.is_valid():
            ### save all data edited ###
            user_form.save()
            profile_form.save()
            ### show message of successfull edit ###
            messages.success(request,'your profile has been updated!')
            ### redirect to profile page ###
            return redirect('profile')
    ### if request method was get then show forms with instance user data  ###
    else:
        user_form = UserEditForm( instance= request.user)
        profile_form = EditProfileForm(instance= request.user.profile)
    ### cantext that will be passed to ui ####
    context = {'user_form':user_form,'profile_form':profile_form,}
    #### render the ui of profile edit ####
    return render(request, 'accounts\profile_edit.html',context)

