from django.urls import path

from . import views
# from . import generic_views
from .api.urls import urlpatterns as api_urls_patterns



app_name = "polls"

try:
    urlpatterns = [
        # ex: /polls/
        path("", generic_views.IndexView.as_view(), name="index"),
    
        # ex: /polls/5/
        path("<int:pk>/", generic_views.DetailView.as_view(), name="detail"),
    
        # ex: /polls/5/results/
        path("<int:pk>/results/", generic_views.ResultsView.as_view(), name="results"),

    ]
except:

    urlpatterns = [
        # ex: /polls/
        path("", views.index, name="index"),
    
        # ex: /polls/5/
        path("<int:pk>/", views.detail, name="detail"),
    
        # ex: /polls/5/results/
        path("<int:pk>/results/", views.results, name="results"),
    
        # create question
        path("question/create/", views.create_question, name="create_question"),

        # update question
        path("question/update/<int:question_id>/", views.update_question, name="update_question"),
    ]

urlpatterns += [
     # ex: /polls/5/vote/
    path("<int:pk>/vote/", views.vote, name="vote"),
] + api_urls_patterns