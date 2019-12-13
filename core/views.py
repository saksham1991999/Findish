from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date

from .models import board_of_members, product, team_members, HomeSlideshow, RandDSlideshow
from .forms import NotifyMeForm, ContactForm
# Create your views here.


def sendmail(receiver, message):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )


def HomeView(request):
    slideshow = HomeSlideshow.objects.all()
    topproducts = product.objects.all()[:4]
    members = team_members.objects.all()[:4]
    context = {
        'slideshow': slideshow,
        'topproducts': topproducts,
        'members': members,
    }
    return render(request, 'home.html', context)

def BaseView(request):
    context = {
    }
    return render(request, 'base.html', context)

def RandDView(request):
    slideshow = HomeSlideshow.objects.all()
    context = {
        'slideshow': slideshow
    }
    return render(request, 'r&d.html', context)

def AboutView(request):
    team = team_members.objects.all()
    context = {
        'members': team
    }
    return render(request, 'about.html', context)

def BODView(request):
    bod = board_of_members.objects.all()
    context = {
        'directors' : bod
    }
    return render(request, 'board_of_directors.html', context)
    
def ProductsView(request):
    products = product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products' : products
    }
    return render(request, 'products.html', context)

def ProductView(request, id):
    individualproduct = product.objects.get(product_id=id)
    products = product.objects.all()[:4]
    context = {
        'product' : individualproduct,
        'products' : products
    }
    return render(request, 'product.html', context)

def ComingSoonView(request):
    return render(request, 'comingsoon.html', {})

def ContactUsView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.date = date.today()
            new_form.receiver = 'findishmail@gmail.com'
            new_form.save()
            send_mail(
                'Findish Contact:',
                " Name :" + new_form.name + " Phone Number: " + new_form.mobile_number + ' country: ' + str(new_form.country) + ' message: ' + new_form.message  ,
                'saksham191999@gmail.com',
                ['saksham1991999@gmail.com'],
                fail_silently=True,
            )
            messages.success(
                            request,
                            'Message Sent Successfully',
                            extra_tags='alert alert-success alert-dismissible fade show'
                            )
            return redirect('core:contact')
    else:
        form = ContactForm()
        context = {
        'form': form
        }
        return render(request, 'contact.html', context)
    
def NotifyView(request):
    if request.method == 'POST':
        print('NOTIFY ME POST METHOD')
        form = NotifyMeForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.date = date.today()
            new_form.save()
            send_mail(
                'Findish Contact:',
                " Name :" + new_form.name + " Phone Number: " + new_form.mobile_number + 'Product' + new_form.product + ' Quantity' + str(new_form.product_quantity) + ' country: ' + str(new_form.country) + ' message: ' + new_form.message  ,
                'saksham191999@gmail.com',
                ['saksham1991999@gmail.com'],
                fail_silently=True,
            )
            messages.success(
                            request,
                            'Message Sent Successfully',
                            extra_tags='alert alert-success alert-dismissible fade show'
                            )
            
            return redirect('core:notify')
    else:
        form = NotifyMeForm()
    context = {
      'form': form
    }
    return render(request, 'notify.html', context)
