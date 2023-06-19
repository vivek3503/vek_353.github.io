from django.db import models

# Create your models here.

class contact_up(models.Model):
  email = models.CharField(max_length=30)
  contact = models.CharField(max_length=13)
  message = models.CharField(max_length=100)
  name = models.CharField(max_length=30)
  
class user(models.Model):
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=10)
  username = models.TextField(max_length=30)
  otp = models.IntegerField(default=1234)
  
class Add_product(models.Model):
  product_id = models.ForeignKey(user,on_delete=models.CASCADE )
  name = models.CharField(max_length=30 ) 
  price = models.IntegerField()
  description = models.CharField(max_length=1000)
  pic = models.ImageField(upload_to='img')


