from rest_framework import serializers

from ..models import Question, Choice

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date",)

class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date", "choices"]