from django.db import models

# Create your models here.


class Instrument(models.Model):
    SN = models.CharField(max_length=30, unique=True)
    Name = models.CharField(max_length=60)

    def __str__(self):
        return self.SN
