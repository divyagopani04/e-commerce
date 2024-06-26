from django.db import models
from django.forms import ModelForm

# Create your models here.

class reg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class maincategory(models.Model):
    category = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

class subcategory(models.Model):
    userid = models.IntegerField(default=0)
    subitem = models.CharField(max_length=100,default=0)
    item = models.CharField(max_length=100)
    substatus = models.IntegerField(default=0)
      
class productdata(models.Model):
    pcategory = models.CharField(max_length=100)
    psubcategory = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank = False, null = False)
    discription = models.CharField(max_length=100, blank = False, null = False)
    price = models.CharField(max_length=100, blank = False, null = False)
    quantity = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    pstatus = models.CharField(max_length=100,default=0)
    image = models.FileField(upload_to='media/',default='')

class imagedata(ModelForm):
    class Meta:
        model = productdata
        fields = ['pcategory','psubcategory','name','discription','price','quantity','discount','image']


class contactinfo(models.Model):
    cname = models.CharField(max_length=100)
    cemail = models.EmailField(max_length=100)
    cphone = models.CharField(max_length=100)
    cbirthdate = models.CharField(max_length=100)
    cclinic = models.CharField(max_length=100)
    cdoctor = models.CharField(max_length=100)
    cmessage = models.CharField(max_length=100)

class billing_details(models.Model):
    bcountry = models.CharField(max_length=100)
    bfirstname = models.CharField(max_length=100)
    blastname = models.CharField(max_length=100)
    bcompanyname = models.CharField(max_length=100)
    baddress = models.CharField(max_length=100)
    bcity = models.CharField(max_length=100)
    bstate = models.CharField(max_length=100)
    bzipcode = models.CharField(max_length=100)
    bemail = models.EmailField(max_length=100)
    bphone = models.CharField(max_length=100)
    bmessage = models.CharField(max_length=100)
    buserid = models.CharField(max_length=100)

class userorder(models.Model):
    ouserid = models.IntegerField(default=0)
    oproductid = models.IntegerField(default=0)
    oproduct = models.CharField(max_length=100)
    oimage = models.FileField(upload_to='media/',default='')
    oprice = models.CharField(max_length=100)
    oquantity = models.IntegerField(default=1)
    ototal = models.CharField(max_length=100)
    odiscount = models.CharField(max_length=100)
