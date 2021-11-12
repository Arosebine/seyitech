from django import urls
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from django.urls import path
from seyitechapp import views
from django.urls.resolvers import URLPattern
from django.urls import path


app_name = 'seyitechapp'


urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('project/', views.project, name='project'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('user_view/<int:prop_id>/', views.user_view, name='user_view')
    
]