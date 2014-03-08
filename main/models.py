from django.db import models
from model_utils.models import TimeStampedModel


class Ask(TimeStampedModel):
    need = models.CharField(max_length=1000)
    fulfilled = models.BooleanField()



class Answer(TimeStampedModel):
	response = models.CharField(max_length=1000)

