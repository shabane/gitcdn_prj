from django.urls import path, include
from .views import ImageViewSet,Base64ImageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('image', ImageViewSet)
router.register('b664image', Base64ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
