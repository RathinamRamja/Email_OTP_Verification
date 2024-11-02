from django.db import models

# Create your models here.

class Otp(models.Model):
    email=models.EmailField()
    otp=models.IntegerField()
    otpexpriedtime=models.CharField(max_length=50)
    
    
