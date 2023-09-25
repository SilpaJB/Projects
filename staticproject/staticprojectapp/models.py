from django.db import models


# Create your models here.
class Place(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()

    def __str__(self):
        return self.Name


class Person(models.Model):
    Name1 = models.CharField(max_length=250)
    Image1 = models.ImageField(upload_to='traveller')
    Details = models.TextField()

    def __str__(self):
        return self.Name1
