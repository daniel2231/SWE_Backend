from django.urls import path, include
from .views import QuestionAPI, unittest_viewAPI, unittest_resultAPI, resultAPI

urlpatterns = [
    path("questions/", QuestionAPI),
    path('questions/<id>/', QuestionAPI),

    path("unittests/", unittest_viewAPI),
    path('unittests/<id>/', unittest_viewAPI),

    path("unittests/result/<id>", unittest_resultAPI),

    path('result/<id>', resultAPI)
]

