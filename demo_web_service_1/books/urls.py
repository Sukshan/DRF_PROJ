from django.urls import path, include
from rest_framework import DefaultRouter
from .view import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]