from django.db import models


def base64validator(b64: str):
    import re
    if not re.fullmatch('^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$', b64):
        raise ValueError('data is not correct base64 data!')


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static')
    cdn_path = models.CharField(max_length=256, blank=False, null=False, default='None')

    def __str__(self):
        return self.name


class Base64Image(models.Model):
    name = models.CharField(max_length=100)
    b64data = models.TextField(unique=True, validators=[base64validator])
    cdn_path = models.CharField(max_length=256, blank=False, null=False, default='None')

    def __str__(self):
        return self.name
