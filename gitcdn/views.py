from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Image
from .serializer import ImageSerializer, ImageSerializerAllField
from rest_framework.response import Response
from gitcdn_prj.settings import SAVE_TO_DB, REPO, OWNER, TOKEN
from .moduls import unamer
from .github import Github
import os
import hashlib


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer_class = ImageSerializer(data=request.data)
        if serializer_class.is_valid():
            file = serializer_class.validated_data["image"].file.read()
            extension = serializer_class.validated_data['image'].name[serializer_class.validated_data['image'].name.find('.'):]
            file_hash = hashlib.md5(file).hexdigest()
            file_name = f'{file_hash}{extension}'

            if SAVE_TO_DB:
                Image.objects.create(name=file_name, image=serializer_class.validated_data['image'])
                #TODO: :/ we should use the hash of file as it saving name

            git = Github(OWNER, REPO, TOKEN)
            file = file
            res = git.insert(f'files/{file_name}', file, f'add image {file_name}')

            if res.status_code != 201:
                return Response({
                    'status_code': res.status_code,
                    'reference': 'https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents--status-codes',
                    'msg': res.json(),
                })

            res = {
                'status': res.status_code,
                'git_url': f"{res.json()['content']['html_url']}?raw=true",
                'path': f'static/{file_name}' if SAVE_TO_DB else 'None',
            }

            return Response(res)
        else:
            return Response(serializer_class.errors)

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({
                'status': '403',
                'msg': 'list images need authenticated user.'
            })

        queryset = Image.objects.all()
        serializer = ImageSerializerAllField(queryset, many=True)
        return Response(serializer.data)
