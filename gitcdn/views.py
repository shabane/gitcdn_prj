from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Image, Base64Image
from .serializer import ImageSerializer, ImageSerializerAllField, Base64ImageSerializer
from rest_framework.response import Response
from gitcdn_prj.settings import SAVE_TO_DB, REPO, OWNER, TOKEN, SAVE_DIR, STATICFILES_DIRS
from .moduls import unamer
from .github import Github
import os
import hashlib
import base64


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
            res = git.insert(f'{SAVE_DIR}/{file_name}', file, f'add image {file_name}')

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


class Base64ImageViewSet(ModelViewSet):
    queryset = Base64Image.objects.all()
    serializer_class = Base64ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = Base64ImageSerializer(data=request.data)
        if not serializer.is_valid():
            return serializer.errors

        b64data = serializer.validated_data['b64data']
        file_name = hashlib.md5(bytes(str(b64data), encoding='utf-8')).hexdigest()
        file = base64.b64decode(b64data)

        git = Github(OWNER, REPO, TOKEN)
        res = git.insert(f'{SAVE_DIR}/{file_name}', b64data, f'add base64 image {file_name}', True)

        if res.status_code != 201:
            resp = {
                'status_code': res.status_code,
                'reference': 'https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents--status-codes',
                'msg': res.json(),
            }
        else:
            resp = {
                'status': res.status_code,
                'git_url': f"{git_url}",
                'path': f'static/{file_name}' if SAVE_TO_DB else 'None',
            }

            git_url = f"{res.json()['content']['html_url']}?raw=true"

        if SAVE_TO_DB:
            for fld in STATICFILES_DIRS:
                with open(f'{fld}/{file_name}', 'wb') as fli:
                    fli.write(file)
                    Base64Image.objects.create(name=file_name, b64data=b64data, cdn_path=git_url)

        return Response(resp)

    def list(self, request, *args, **kwargs):
        queryset = Base64Image.objects.all()
        serializer_class = Base64ImageSerializer

        if not request.user.is_authenticated:
            return Response({
                'status': 403,
                'msg': 'you dont have permission to view images',
            })

        data = {}

        for img in queryset:
            # data[img['name']] = img['b64data']
            print(img)

        return Response(data)