from django.db import models

# Create your models here.


class Instrument(models.Model):
    SN = models.CharField(max_length=30, unique=True)  # 장비 SN
    Name = models.CharField(max_length=60)  # 장비명

    def __str__(self):
        return self.SN
