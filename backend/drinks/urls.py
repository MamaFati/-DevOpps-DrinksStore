from .views import *
from django.urls import path


urlpatterns = [
    path('',GetAllDrinks.as_view()),
    path('<int:pk>/',GetSingleDrink.as_view()),
    path("create/",CreateDrink.as_view()),
    path("delete/<int:pk>",DeleteDrink.as_view()),
    path("update/<int:pk>",UpdateDrinks.as_view())
]