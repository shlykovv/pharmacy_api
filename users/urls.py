from django.urls import path

from users.views import RegisterView, ProfileView


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
]
