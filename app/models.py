from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=111)
    phone=models.CharField(max_length=111)
    desc=models.TextField(default='write description')

