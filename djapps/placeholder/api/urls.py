from django.urls import path 

from .views import ListView

app_name = "placeholder_api"

urlpatterns = [
    path("", ListView.as_view(), name="list")
]
