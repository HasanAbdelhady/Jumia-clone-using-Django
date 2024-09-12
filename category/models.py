from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name  # This will show the name of the category in the admin panel
