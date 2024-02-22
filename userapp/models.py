from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class drinks(models.Model):
    Drinks=models.CharField(max_length=50)
    Image=models.ImageField()
    Qty=models.CharField(max_length=10)
    Price=models.IntegerField()
    Discription=models.TextField()
    def __str__(self):
        return self.Drinks
class customuser(AbstractUser):
    pass 
    
   
