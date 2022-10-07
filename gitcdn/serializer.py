from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Image


class ImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class ImageSerializerAllField(HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'name', 'cdn_path', 'id']
