from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date

# Create your views here.

def HomeView(request):
	context = {}
	return render(request, 'home.html', context)

