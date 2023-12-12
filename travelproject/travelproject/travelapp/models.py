from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    Img = models.ImageField(upload_to='pics')
    Name = models.CharField(max_length=250)
    Desc = models.TextField()

    def __str__(self):
        return self.Name
