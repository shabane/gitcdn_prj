from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Image
from .serializer import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
