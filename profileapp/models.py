from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # 1:1 매칭 시켜준다. User 와 Profile 1:! 매칭
    # related_name = request.user.profile.nickname
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    name = models.CharField(max_length=20, unique=True, null=True)