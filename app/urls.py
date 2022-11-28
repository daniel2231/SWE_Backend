from django.urls import path, include
from .views import QuestionAPI

urlpatterns = [
    path("questions/", QuestionAPI),
    path('questions/<id>/', QuestionAPI),
]