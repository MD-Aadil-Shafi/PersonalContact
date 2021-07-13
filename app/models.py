from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    info = models.CharField(max_length=200,blank=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=60)
    gender = models.CharField(max_length=7, choices=(
        ('Male','male'),
        ('Female','female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-pk']


class Message(models.Model):
    manager = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    subject = models.CharField(max_length=60)
    description = models.TextField(max_length=600)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-pk']