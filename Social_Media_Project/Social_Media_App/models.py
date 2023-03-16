from django.db import models
from django.contrib.auth.models import auth,User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.CharField(max_length=250, null=True)
    profile_pic=models.ImageField(upload_to="profile_images")
    date_time=models.DateTimeField(auto_now_add=True, null=True)    

