from django.urls import path

from rest_framework.routers import DefaultRouter

from profiles.views import *


urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('create/', CreateProfileView.as_view()),
    path('login/', LoginProfileView.as_view())
]
