from django.urls import path
from .views import *


urlpatterns = [
    path('signup/',signup,name= 'signup'),
    path('profile/',show_profile,name= 'profile'),
    path('profile/edit/',edit_profile,name= 'edit_profile'),
]
