
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('why_ecoyan', views.why_ecoyan, name='why_ecoyan'),
    path('certification', views.certification, name='certification'),
    path('customers', views.customers, name='customers'),
    path('photos', views.photos, name='photos'),
    path('e_rickshaw', views.e_rickshaw, name='e_rickshaw'),
    path('e_cargo', views.e_cargo, name='e_cargo'),
    path('e_garbage', views.e_garbage, name='e_garbage'),
    path('golf_cart', views.golf_cart, name='golf_cart'),
    path('car', views.car, name='car'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

    