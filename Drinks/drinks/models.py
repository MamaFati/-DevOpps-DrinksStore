# we import django.db ie django database into our models
from django.db import models

# create a class for our project the models.Model helps django identfy our model as a model classs
# meaning each drink should have a name and a discription
# To create a database from this information, we need to perform another migration
class Drinks(models.Model):
    # creating our entities
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.name + ' ' + self.description