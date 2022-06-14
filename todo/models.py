from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
  title = models.CharField(max_length=500)
  user = models.ForeignKey(User,max_length=100,on_delete=models.CASCADE,default=False)

  def __str__(self):
    return self.title