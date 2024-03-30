from django.shortcuts import render , redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate , login

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
            return redirect('/jobs/')
    ### if request metod is get ###
    else:
        form = SignUpForm()

    return render(request,'registration\sign_up.html',{'form':form})
