from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, default=None)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(max_length=500, blank=True)
    phone_numer = models.CharField(max_length=15, blank=True)

    picture = models.ImageField(upload_to = 'users/pictures', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username