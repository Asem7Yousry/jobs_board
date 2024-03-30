from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .models import Profile

###### form to sign up #######
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

### form to edit profile data of user ###
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number','image','city']

### form to edit user data ###
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name' , 'email']

