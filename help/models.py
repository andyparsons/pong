from django.db import models
from model_utils.models import TimeStampedModel


class Ask(TimeStampedModel):
    db_table = 'ask'
    body = models.CharField(max_length=1000)
    is_closed = models.BooleanField(default=False)



class Answer(TimeStampedModel):
    db_table = 'answer'
    body = models.CharField(max_length=1000)
    ask = models.ForeignKey(Ask)

