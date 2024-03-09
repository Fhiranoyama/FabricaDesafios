from django.urls import path
from .views import Dieta

urlpatterns = [
    path('nutri/', Dieta.as_view()),
]