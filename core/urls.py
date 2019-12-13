from django.urls import path
from .views import HomeView, BaseView, AboutView, BODView, RandDView, ProductsView, ProductView, ComingSoonView, ContactUsView, NotifyView

app_name = 'core'

urlpatterns = [
    path('', HomeView, name='home'),
    path('base/', BaseView, name='base'),
    path('bod/', BODView, name='bod'),
    path('about/', AboutView, name='about'),
    path('products/', ProductsView, name='products'),
    path('products/<id>', ProductView, name='product'),
    path('r&d/', RandDView, name='r&d'),
    path('notify/', NotifyView, name='notify'),
    path('contact/', ContactUsView, name='contact'),

    path('checkout/', HomeView, name='checkout'),
    path('order-summary/', HomeView, name='order-summary'),
    path('product/<slug>/', HomeView, name='product'),
    path('add-to-cart/<slug>/', HomeView, name='add-to-cart'),
    path('add-coupon/', HomeView, name='add-coupon'),
    path('remove-from-cart/<slug>/', HomeView, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', HomeView,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', HomeView, name='payment'),
    path('request-refund/', HomeView, name='request-refund')
]
