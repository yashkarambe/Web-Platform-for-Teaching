from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    def __str__(self):
        return self.question_text
    def was_publish_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    Choice_1 = models.CharField(max_length=200)
    Choice_2 = models.CharField(max_length=200)
    Choice_3 = models.CharField(max_length=200)
    Choice_4 = models.CharField(max_length=200)
    Choice_true = models.CharField(max_length=200)
    def __str__(self):
        return self.Choice_true
        