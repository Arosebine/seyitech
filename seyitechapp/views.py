from django.shortcuts import render
from django.contrib.auth.models import User
from seyitechapp.form import *

from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.


def user_view(request, prop_id):
    user = User.objects.all(id=prop_id)
    return render(request, 'public/blog.html', {'user_key': user })



def index(request):
    return render(request, 'public/index.html', {})


def about(request):
    return render(request, 'public/about.html')


def blog_detail(request):
    return render(request, 'public/blog-detail.html')



def blog(request):
    return render(request, 'public/blog.html')



def contact(request):
    return render(request, 'public/contact.html')



def product_detail(request):
    return render(request, 'public/product-detail.html')



def project(request):
    return render(request, 'public/projects-masonry.html')



def services(request):
    return render(request, 'public/services-dark.html')


def shop(request):
    return render(request, 'public/shop.html')



def team(request):
    return render(request, 'public/team.html')



def testimonial(request):
    return render(request, 'public/testimonials.html')




    