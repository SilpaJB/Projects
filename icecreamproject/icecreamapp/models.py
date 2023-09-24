from django.db import models


# Create your models here.
class icecream(models.Model):
    name = models.CharField(max_length=250)
    details = models.TextField()
    flavours = models.TextField()
    image=models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name
