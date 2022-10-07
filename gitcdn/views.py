from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Image
from .serializer import ImageSerializer
from rest_framework.response import Response
from gitcdn_prj.settings import SAVE_TO_DB
from .moduls import unamer
from .github import Github
import os
import base64


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer_class = ImageSerializer(data=request.data)
        if serializer_class.is_valid():
            extension = serializer_class.validated_data['image'].name[serializer_class.validated_data['image'].name.find('.'):]
            file_name = f'{unamer()}{extension}'
            token = os.getenv('TOKEN', '<or hard code your token here>')

            if SAVE_TO_DB:
                Image.objects.create(name=file_name, image=serializer_class.validated_data['image'])

            git = Github('bit-orbit', 'CDN', token)
            file = serializer_class.validated_data['image'].file.read()
            res = git.insert(f'files/{file_name}', file, f'add image {file_name}')

            res = {
                'status': res.status_code,
                'git_url': f"{res.json()['content']['html_url']}?raw=true",
                'path': f'static/{file_name}' if SAVE_TO_DB else 'None',
            }

            return Response(res)
        else:
            return Response(serializer_class.errors)
