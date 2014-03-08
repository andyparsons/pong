from django.db import models
from model_utils.models import TimeStampedModel


class Ask(TimeStampedModel):
    body = models.CharField(max_length=1000)
    fulfilled = models.BooleanField()



class Help(TimeStampedModel):
	body = models.CharField(max_length=1000)

