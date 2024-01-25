from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TeacherQuestion, QGPTQuestion

class TeacherQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherQuestion
        fields = ['id', 'user', 'source', 'title', 'problem', 'question_text', 'appendix', 'image']

class QGPTQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QGPTQuestion
        fields = ['id', 'user', 'source', 'title', 'problem', 'question_text']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    