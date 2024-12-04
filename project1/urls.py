from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('user_validation', views.user_verification, name= "user-verification"),
    path('bot-api', views.get_response, name = "chat-bot")
]