from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Inspection(models.Model):
    # 1:1 매칭 시켜준다. User 와 Profile 1:! 매칭
    # related_name = request.user.profile.nickname
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Instrument_SN = models.CharField(max_length=50, null=False)
    Inspector = models.CharField(max_length=20, null=True)
    Start_Date = models.DateField(null=True)
    Completed_Date = models.DateField(null=True)
    Status = models.CharField(max_length=20, null=True)
    Revision = models.CharField(max_length=50, null=True)
    SW_Version = models.CharField(max_length=50, null=True)
    FV2_Version = models.CharField(max_length=50, null=True)
    FW_PipetteCh = models.CharField(max_length=50, null=True)
    FW_Xdrive = models.CharField(max_length=50,null=True)
    FW_Master = models.CharField(max_length=50,null=True)
    Computer_SN = models.CharField(max_length=50,null=True)






