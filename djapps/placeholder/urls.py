from django.urls import path 

from . import views 
from .api import views as api_views


app_name = "placeholder"

urlpatterns = [
    path("<int:id>/", views.get_user, name="index"),
    path("", views.index, name="index"),
    path("api/", api_views.ListView.as_view(), name="api_index"),
    # 
    path("gen", views.addview, name="gen"),
    path("result/<str:id>/", views.resultview, name="result"),
    path("status/<str:id>/", views.statusview, name="status")
]
