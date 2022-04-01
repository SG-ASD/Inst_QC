from django.db import models

# Create your models here.


class Category(models.Model):
    Category = models.CharField(max_length=30)
    Subcategory = models.CharField(max_length=60)

    def __str__(self):
        return self.Category
