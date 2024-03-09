from django.urls import path
from .views import Dieta, updel


urlpatterns = [
    path('nutri/', Dieta.as_view()),
     path('update-item/<int:item_id>', updel.as_view()),
]
