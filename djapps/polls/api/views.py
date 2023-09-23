from rest_framework import views, generics

from . import serializers
from ..models import Question

class IndexView(generics.ListAPIView):
    serializer_class = serializers.QuestionsSerializer
    queryset = Question.objects.all()

class QuestionView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.QuestionSerializer
    lookup_field = "pk"
    queryset = Question.objects.all()