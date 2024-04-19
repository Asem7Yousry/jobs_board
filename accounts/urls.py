from django.urls import path
from .views import *


urlpatterns = [
    # path('signup/',signup,name= 'signup'),
    path('signup/',SignUp.as_view(),name= 'signup'),
    # path('profile/',show_profile,name= 'profile'),
    path('profile/',Profile_View.as_view(),name= 'profile'),
    path('profile/edit/',edit_profile,name= 'edit_profile'),
]
