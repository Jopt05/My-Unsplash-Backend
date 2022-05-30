from django.urls import path

from images import views

urlpatterns = [
    path('', views.Images.as_view()),
    path('<int:pk>', views.ImagesByUser.as_view()),
]
