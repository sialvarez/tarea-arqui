from django.db import models

# Create your models here.

class Comment(models.Model):
   
    choice_text = models.CharField(max_length=150)
    ip = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add=True)
