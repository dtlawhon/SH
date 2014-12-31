from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    #user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
   # sex = models.CharField(max_length=50, blank=True)
   # phone_number =
   # birthday =
   # location =
   # about_me = models.TextField(max_length=500, blank=True, null = True)
   # school = models.CharField(max_length=50, blank=True)
   # work = 
   # time_zone = 
   # languages = 
   # emergency_contact = 
    

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


"""
class Chef(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    join_date = models.DateTimeField('date joined')
    def __unicode__(self):
        return self.email
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    join_date = models.DateTimeField('date joined')
    def __unicode__(self):
        return self.email   """
    

