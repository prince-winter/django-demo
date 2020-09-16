from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Post(models.Model):
    text = models.TextField(max_length=200, unique=True) 

    def __str__(self):
        return self.text 

class Author(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
 
    def __str__(self): 
        return self.name 
 
class Date(models.Model):
    name = models.ForeignKey(Author, on_delete= models.CASCADE)
    date = models.DateField() 
  
    def __str__(self):    
        return str(self.date)

    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # adding your personal attributes
    portfolio_site = models.CharField(blank=True, max_length=50)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
