from django.db import models


class Testimation(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True )


    def __str__(self):
        return self.name
    