from .views import CustomAuthToken
from django.urls import path

urlpatterns = [
    path('', CustomAuthToken.as_view()),
]
