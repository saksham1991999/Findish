from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date

from .models import post, like, comment, categories

# Create your views here.

def BlogHomeView(request):
    all_categories = categories.objects.all()
    all_posts = post.objects.order_by('-date')
    context = {
        'categories': all_categories,
        'posts': all_posts,
    }
    return render(request, 'bloghome.html', context)


def BlogPostView(request, slug):
    slug_post = post.objects.filter(slug=slug)[0]
    print(slug_post)
    comments = comment.objects.filter(post = slug_post)
    all_categories = categories.objects.all()
    context = {
        'post': slug_post,
        'comments': comments,
        'categories': all_categories,
    }
    return render(request, 'blogpost.html', context)
