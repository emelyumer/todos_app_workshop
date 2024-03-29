from django.shortcuts import render
from rest_framework import generics as api_views, serializers

from todos_app_workshop.todos.models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Todo
        fields = '__all__'


class TodoListCreateApiView(api_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

