from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class Ask(TimeStampedModel):
    db_table = 'ask'
    user = models.ForeignKey(User)
    body = models.CharField(max_length=1000)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:10]


class Answer(TimeStampedModel):
    db_table = 'answer'
    user = models.ForeignKey(User)
    body = models.CharField(max_length=1000)
    ask = models.ForeignKey(Ask)

    def __str__(self):
        return self.body[:10]

