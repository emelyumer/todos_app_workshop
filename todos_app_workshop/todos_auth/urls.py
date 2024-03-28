from django.urls import path

from todos_app_workshop.todos_auth.views import CreateUserApiView

urlpatterns = (
    path('register/', CreateUserApiView.as_view(), name='api_create_user'),

)