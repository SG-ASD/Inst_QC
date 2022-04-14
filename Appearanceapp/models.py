from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from django.db import models
#
# # Create your models here.
#
#
class Appearance(models.Model):
    # 1:1 매칭 시켜준다. User 와 Profile 1:! 매칭
    # related_name = request.user.profile.nickname
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Instrument_SN = models.CharField(max_length=50, null=False)
    Shock_Watch = models.CharField(max_length=20, null=True)
    Binding = models.CharField(max_length=20, null=True)
    Labels = models.CharField(max_length=20, null=True)
    Packaging_Box = models.CharField(max_length=20, null=True)
    Wooden_Pallet = models.CharField(max_length=20, null=True)
    Transport_Jig = models.CharField(max_length=20, null=True)
    Shock_Watch_Image = models.ImageField(upload_to='Appearance/', null=True)
    Binding_Image = models.ImageField(upload_to='Appearance/', null=True)
    Labels_Image = models.ImageField(upload_to='Appearance/', null=True)
    Packaging_Box_Image = models.ImageField(upload_to='Appearance/', null=True)
    Wooden_Pallet_Image = models.ImageField(upload_to='Appearance/', null=True)
    Transport_Jig_Image = models.ImageField(upload_to='Appearance/', null=True)
    Video = models.FileField(upload_to="video/", null=True)
    # Front = models.CharField(max_length=20, null=True)
    # Right = models.CharField(max_length=20, null=True)
    # Left = models.CharField(max_length=20, null=True)
    # Back = models.CharField(max_length=20, null=True)
    # Acc_Damage = models.CharField(max_length=20, null=True)
    # Acc_Missing = models.CharField(max_length=20, null=True)




