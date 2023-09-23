from django.urls import path, include

from . import views

urlpatterns = [
    path("api/", views.IndexView.as_view(), name="index_api"),
    path("api/<int:pk>/", views.QuestionView.as_view(), name="question")
]
