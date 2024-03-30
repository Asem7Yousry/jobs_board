from django.db import models
from django.contrib.auth.models import User
### import PhoneNumberField ###
from phonenumber_field.modelfields import PhoneNumberField
### import for reciver decorator ####
from django.dispatch import receiver
#### import post_save signal #####
from django.db.models.signals import post_save

### function to get image and save it by its name and extention to media folder
def upload_img(instance , filename):
    ### split file name to name and extention to get and save extention of uplaoded image 
    imagename , extention = filename.split(".")
    ### return the path of saved uplauded image 
    return f"profile/{instance}.{extention}"

#### model for profile ####
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    phone_number = PhoneNumberField()
    image = models.ImageField(upload_to= upload_img, null=True , blank=True)
    city = models.ForeignKey('cities_light.City', on_delete= models.SET_NULL , null= True , blank= True)

    ### to show each profile by its user name ###
    def __str__(self):
        return f'{self.user.username}'

#### signal to create profile automaticlly when new user ceated (sign up) ######
@receiver(post_save, sender=User)
def create_new_profile(sender, instance , created , **kwargs):
    ### check if new user created #####
    if created:
        #### create new object of profile for the saved user #####
        Profile.objects.create(user= instance)

