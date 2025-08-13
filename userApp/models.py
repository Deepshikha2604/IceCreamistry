from django.db import models

import uuid
class profile(models.Model):
    userName=models.CharField(max_length=100)
    featured_image=models.ImageField(null=True, blank=True, upload_to='profileimg/', default='profileimg/default.jpg')
    userProfession=models.CharField(max_length=100, null=True, blank=True)
    user_phone=models.CharField(max_length=100, null=True, blank=True)
    user_email=models.CharField(max_length=100, null=True, blank=True)
    user_address=models.CharField(max_length=100, null=True, blank=True)
    userFeedback=models.TextField(null=True, blank=True)

    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.userName) 
        

# Create your models here.
