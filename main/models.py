from django.db import models


class Ask(models.Model):
    need = models.CharField(max_length=1000)
    fulfilled = models.BooleanField()
