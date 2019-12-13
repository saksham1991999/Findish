from django.db import models
from django_countries.fields import CountryField

class board_of_members(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    contact = models.CharField(max_length  = 50)
    description = models.TextField(blank = True, null=True)
    image = models.ImageField(blank = True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Board Of Members'

class product(models.Model):
    product_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True, null=True)
    category = models.CharField(max_length = 25)
    label = models.CharField(max_length = 25)
    price = models.FloatField()
    main_image = models.ImageField()
    image1 = models.ImageField(blank = True, null=True)
    image2 = models.ImageField(blank = True, null=True)
    image3 = models.ImageField(blank = True, null=True)
    image4 = models.ImageField(blank = True, null=True)

    def __str__(self):
        return self.title

class team_members(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    contact = models.CharField(max_length  = 50)
    description = models.TextField(blank = True, null=True)
    image = models.ImageField(blank = True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Team Members'

class notisfication(models.Model):
    name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    mobile_number = models.CharField(max_length = 15)
    whatsapp_number = models.CharField(max_length = 15)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    street_address = models.CharField(max_length = 25)
    city = models.CharField(max_length = 15)
    pincode = models.CharField(max_length = 6)
    country = CountryField()
    message = models.TextField(blank = True, null = True)
    date = models.DateField(blank = True, null = True)

class message(models.Model):
    receiver = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    mobile_number = models.CharField(max_length = 15)
    whatsapp_number = models.CharField(max_length = 15)
    street_address = models.CharField(max_length = 25, blank = True, null = True)
    city = models.CharField(max_length = 15, blank = True, null = True)
    pincode = models.CharField(max_length = 6, blank = True, null = True)
    country = CountryField()
    message = models.TextField()
    date = models.DateField()

class HomeSlideshow(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 100, blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name_plural = 'Home Slideshow'

class RandDSlideshow(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 100, blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name_plural = 'R&D Slideshow'

#from django.core.validators import RegexValidator
#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")