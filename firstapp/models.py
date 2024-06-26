from django.db import models

# Create your models here.

class registerfront(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class cart(models.Model):
    userid = models.IntegerField(default=0)
    productid = models.IntegerField(default=0)
    product = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/',default='')
    price = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    total = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)

class customerreview(models.Model):
    userid = models.IntegerField(default=0)
    productid = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=100)
    rname = models.CharField(max_length=100)
    remail = models.CharField(max_length=100)



