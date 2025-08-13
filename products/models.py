from django.db import models
import uuid
class chef(models.Model):
    chefName=models.CharField(max_length=100)
    featured_image=models.ImageField(null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    designation=models.CharField(max_length=100, null=True, blank=True)
    social_fb=models.CharField(max_length=100, null=True, blank=True)
    social_x=models.CharField(max_length=100, null=True, blank=True)
    social_ld=models.CharField(max_length=100, null=True, blank=True)

    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.chefName
    
class iceCream(models.Model):
    iCream_price=models.IntegerField()
    iCream_image=models.ImageField(null=True, blank=True)
    iCream_name=models.CharField(max_length=100)

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.iCream_name
    
class Services(models.Model):
    Service_name=models.CharField(max_length=100)
    Service_description=models.TextField(null=True, blank=True)
    Service_image=models.ImageField(null=True, blank=True)

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.Service_name

class contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.CharField(max_length=100, null=True, blank=True)
    contact_subject=models.CharField(max_length=100, null=True, blank=True)
    contact_query=models.TextField(null=True, blank=True)

    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.contact_name) 
        

# Create your models here.
