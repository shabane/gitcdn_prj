from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static')
    cdn_path = models.CharField(max_length=256, blank=False, null=False, default='None')

    def __str__(self):
        return self.name
