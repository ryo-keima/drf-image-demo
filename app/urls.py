from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ImageViewSet

router = DefaultRouter()
router.register(r'image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
