from django.urls import path, include
from .views import registration

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('registration/', registration, name='registration'),
]
