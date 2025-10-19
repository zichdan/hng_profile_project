# profile_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This pattern routes requests to the root of the app ('/me') to the get_profile view.
    path('me/', views.get_profile, name='get_profile'),
]