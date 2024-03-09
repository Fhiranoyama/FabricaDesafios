from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .Api.viewsets import FactoryViewSet

router = DefaultRouter()
router.register(prefix="nutri", viewset=FactoryViewSet)


urlpatterns = [
    path("Api/", include(router.urls))
]