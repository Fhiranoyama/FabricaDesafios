from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import FactoryViewSet

router = DefaultRouter()
router.register(prefix="nutri", viewset=FactoryViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]