from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=140, null=True) 
    website_url = models.URLField("Website", blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])