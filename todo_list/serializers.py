from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Comment,Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class TaskSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = [
            'id', 
            'user', 
            'user_name', 
            'title', 
            'description', 
            'created_at', 
            'due_date', 
            'status', 
            'is_archived'
        ]
        read_only_fields = ['created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) # Vazifa bilan birga izohlarni ham ko'rish uchun
    class Meta:
        model = Task
        fields = '__all__'