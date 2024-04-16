# In urls.py

from django.urls import path
from django.http import HttpResponse

# Import your views module
from . import views

# Define a view to serve the sitemap.xml file
def sitemap_xml(request):
    # Read the sitemap.xml file
    with open('sitemap.xml', 'r') as file:
        sitemap_xml = file.read()
    return HttpResponse(sitemap_xml, content_type='application/xml')

from django.urls import path
from django.http import HttpResponse

# Define a view to serve the robots.txt file
def robots_txt(request):
    # Read the robots.txt file
    with open('robots.txt', 'r') as file:
        robots_txt = file.read()
    return HttpResponse(robots_txt, content_type='text/plain')

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('success', views.success_view, name='success'),
    path('why_ecoyan', views.why_ecoyan, name='why_ecoyan'),
    path('certification', views.certification, name='certification'),
    path('customers', views.customers, name='customers'),
    path('photos', views.photos, name='photos'),
    path('e_rickshaw', views.e_rickshaw, name='e_rickshaw'),
    path('e_cargo', views.e_cargo, name='e_cargo'),
    path('e_garbage', views.e_garbage, name='e_garbage'),
    path('golf_cart', views.golf_cart, name='golf_cart'),
    path('car', views.car, name='car'),
    # Define the URL pattern for sitemap.xml
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
    path('robots.txt', robots_txt, name='robots_txt'),
]

