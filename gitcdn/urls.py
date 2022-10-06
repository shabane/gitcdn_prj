from django.urls import path, include
from .views import ImageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
