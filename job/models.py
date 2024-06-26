from django.db import models
from django.utils.text import slugify

######## create all models for the job app ########

#### tuple to choose 2 types of job type ####
JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time'),
)

### function to get image and save it by its name and extention to media folder
def upload_img(instance , filename):
    ### split file name to name and extention to get and save extention of uplaoded image 
    imagename , extention = filename.split(".")
    ### return the path of saved uplauded image 
    return f"jobs/{instance}.{extention}"

### function to get cv from user and save it by its name and extention to media folder
def upload_cv(instance , filename):
    ### split file name to name and extention to get and save extention of uplaoded image 
    imagename , extention = filename.split(".")
    ### return the path of saved uplauded image 
    return f"apply/{instance}.{extention}"

## model for job object ##
class Job(models.Model):
    title = models.CharField(max_length = 50)
    job_type = models.CharField(max_length= 15 , choices= JOB_TYPE , default= "full time")
    description = models.CharField(max_length= 500)
    published_date = models.DateTimeField(auto_now= True)
    Vacancy = models.IntegerField(default= 1)
    salary = models.FloatField(default= 0)
    category = models.ForeignKey('Category' , on_delete= models.CASCADE )
    experience_years = models.IntegerField(default= 1)
    image = models.ImageField(upload_to= upload_img)
    slug = models.SlugField(null= True, blank= True)
    
    ### link slug of job by its title for url call by override save method ###
    def save(self, *args , **kwargs):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs)

    ### method to show each job by its name 
    def __str__(self):
        return self.title
        
## model for category of job ##
class Category(models.Model):
    title = models.CharField(max_length= 50)

    ### method to show each job by its name 
    def __str__(self):
        return self.title

## model for application ##
class Application(models.Model):
    name = models.CharField(max_length= 50)
    job = models.ForeignKey(Job,on_delete= models.CASCADE , related_name= 'apply')
    email = models.EmailField(max_length= 50)
    website = models.URLField()
    cv = models.FileField(upload_to= upload_cv)
    coverletter = models.TextField(max_length= 5000)
    date = models.DateField(auto_now= True)

    ### method to show each application qith its user name ###
    def __str__(self):
        return self.name

