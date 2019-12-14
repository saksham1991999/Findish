from django.urls import path
from .views import HomeView

app_name = 'blog'

urlpatterns = [
    path('', HomeView, name='home'),
]
