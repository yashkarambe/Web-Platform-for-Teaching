from django.db import models
from datetime import datetime


# Create your models here.
class log_in_registtration(models.Model):
    Email = models.EmailField(max_length=30)
    password = models.TextField(max_length=20)
    account_type = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.Email
        

        