from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import product, message, notisfication
from django.utils.translation import gettext_lazy as _
from core.models import message, notisfication, product
from core import models

class NotifyMeForm(forms.ModelForm):
    
    class Meta:
        #productsqs = product.objects.all().values('title')
        #productchoice = list(productindividual['title'] for productindividual in productsqs)
        #'product_quantity': forms.Select(choices=productsqs, attrs={'min': '100', 'class': 'custom-select d-block w-100', 'style':"margin-bottom: 25px"})
        model = notisfication
        fields = ['name', 'sender_email', 'mobile_number', 'whatsapp_number', 'product', 'product_quantity', 'street_address', 'city', 'pincode', 'country', 'message']
        labels = {
            'name': _("Full Name"),
            'sender_email': _('Email ID'), 
            'mobile_number' : _("Mobile Number"), 
            'whatsapp_number': _('Whatsapp Number'), 
            'product': _('Select Product'),
            'product_quantity': _('Product Quantity'),
            'street_address': _('Delivery Address'), 
            'city': _('City'), 
            'pincode': _('Pincode'), 
            'country': _('Country'), 
            'message': _('Message'),
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
            'country': CountrySelectWidget(attrs={'class': 'custom-select d-block w-100', 'style':"margin-bottom: 25px"}),
            'product_quantity': forms.NumberInput(attrs={'min': '100', 'class': 'custom-select d-block w-100', 'style':"margin-bottom: 25px"}),
            
        }

        def clean_sender_email(self):
            email = self.cl

class ContactForm(forms.ModelForm):

    class Meta:
        model = message
        fields = ['name', 'sender_email', 'mobile_number', 'whatsapp_number', 'street_address', 'city', 'pincode', 'country', 'message']
        labels = {
            'name': _("Full Name"),
            'sender_email': _('Email ID'), 
            'mobile_number' : _("Mobile Number"), 
            'whatsapp_number': _('Whatsapp Number'), 
            'street_address': _('Address'), 
            'city': _('City'), 
            'pincode': _('Pincode'), 
            'country': _('Country'), 
            'message': _('Message'),
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
            'country': CountrySelectWidget(attrs={'class': 'custom-select d-block w-100', 'style':"margin-bottom: 25px"})
        }

        def clean_sender_email(self):
            email = self.cleaned_data('sender_email')
            return email 
   

class RegisterUserForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length=100, min_length=5)
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Password', max_length=100, min_length=6, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Re-enter Password', max_length=100, min_length=6, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data('email')
        #VALIDATING EMAIL IN DATABASE
        qs = User.objects.filter(email=self.email)
        if qs.exists():
            raise ValidationError('Email is already in use')
        return email    