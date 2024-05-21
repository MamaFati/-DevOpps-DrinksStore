from django.db import models

# Create your models here.
class Drinks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name + ' ' + self.description
