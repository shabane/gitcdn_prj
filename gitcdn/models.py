from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name
