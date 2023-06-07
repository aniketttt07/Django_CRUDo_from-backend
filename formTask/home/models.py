from django.db import models



# Create your models here.

class Profile(models.Model):
    # Field for storing the details of the profile
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.name        # String representation of the profile object
    