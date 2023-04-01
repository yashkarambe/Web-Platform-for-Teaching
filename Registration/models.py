from django.db import models
from datetime import datetime


# Create your models here.
class log_in_registtration_student(models.Model):
    User_name = models.TextField(max_length=20)
    Email = models.EmailField(max_length=30)
    password = models.TextField(max_length=20)
    account_type = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.Email
        

class log_in_registtration_teacher(models.Model):
    User_name = models.TextField(max_length=20)
    Email = models.EmailField(max_length=30)
    password = models.TextField(max_length=20)
    account_type = models.CharField(max_length = 10)
    def __str__(self):
        return self.User_name
    
class thumnail(models.Model):
    product_id = models.AutoField
    playlist_name = models.TextField(max_length=30)
    Chapter_name = models.TextField(max_length=30)
    Topic_name = models.TextField(max_length=30)
    Thumnail_image = models.ImageField(upload_to="Registration/playlist/thumnail")
    Short_Desc = models.TextField(max_length=500)
    pub_date = models.DateField()
    def __str__(self):
        return self.playlist_name
    
class Playlist(models.Model):
    Chapter_name_playlist = models.TextField(max_length=30) 
    Topic_name_playlist = models.TextField(max_length=30) 
    Leactur_title = models.TextField(max_length=30) 
    Desc_leactur = models.TextField(max_length=30) 
    Upload_leactur = models.FileField(upload_to='Registration/video')
    def __str__(self):
        return self.Leactur_title
    
    
class Quize_thumnail(models.Model):
    Quize_name = models.CharField(max_length=30)
    chaptr_name = models.CharField(max_length=30)
    topic_name = models.CharField(max_length=30)
    thumnail = models.ImageField(upload_to="Registration/Quize/thumnail")    
    marks_per_que = models.TextField(max_length=2)
    descreption = models.CharField(max_length=500)
    def __str__(self):
        return self.Quize_name