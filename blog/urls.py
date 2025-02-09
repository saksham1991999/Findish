from django.urls import path
from .views import BlogHomeView, BlogPostView

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView, name='home'),
    path('<slug>', BlogPostView, name='post'),
]
