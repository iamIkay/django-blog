from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length= 50)
    content= models.CharField(max_length= 1000)
    date= models.DateTimeField(default=datetime.now, blank=True)