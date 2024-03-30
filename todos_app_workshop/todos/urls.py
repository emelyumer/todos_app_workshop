from django.urls import path

from todos_app_workshop.todos.views import TodoListCreateApiView, CategoriesListApiView

urlpatterns = [
    path('', TodoListCreateApiView.as_view(), name='api_list_create_todos'),
    path('categories/', CategoriesListApiView.as_view(), name='api_list_categories'),


]