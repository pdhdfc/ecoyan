# In urls.py

from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap
# Import your views module

# Define a view to serve the sitemap.xml file
# def sitemap_xml(request):
#     # Read the sitemap.xml file
#     with open('sitemap.xml', 'r') as file:
#         sitemap_xml = file.read()
#     return HttpResponse(sitemap_xml, content_type='application/xml')


from .sitemaps import StaticViewSitemap, BlogPostSitemap, JobDetailSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogPostSitemap,
    'jobs': JobDetailSitemap,
}

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
    path('dealer', views.dealer, name='dealer'),
    path('book_test_ride', views.book_test_ride, name='book_test_ride'),
    path('success', views.success_view, name='success'),
    path('why_ecoyan', views.why_ecoyan, name='why_ecoyan'),
    # path('certification', views.certification, name='certification'),
    # path('customers', views.customers, name='customers'),
    path('photos', views.photos, name='photos'),
    path('e_rickshaw', views.e_rickshaw, name='e_rickshaw'),
    path('e_cargo', views.e_cargo, name='e_cargo'),
    path('e_garbage', views.e_garbage, name='e_garbage'),
    path('golf_cart', views.golf_cart, name='golf_cart'),
    # path('car', views.car, name='car'),
    # Define the URL pattern for sitemap.xml
    # path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),

    path('blogs', views.blogs, name='blogs'),
    # path('blogs/<int:post_id>/', views.blogs_details, name='blog_details'),
    # path('blogs<slug:slug>', views.blogs_details, name='blog_details'),
    path('blogs/<slug:slug>', views.blogs_details, name='blogpost_detail'),  # Update this line
    
    path('job_list', views.job_list, name='job_list'),
    path('job/<slug:slug>', views.job_detail, name='job_detail'),
    path('job/<slug:slug>/apply', views.apply_for_job, name='apply_for_job'),

    path('PrivacyPolicy', views.PrivacyPolicy, name='PrivacyPolicy'),
    path('TermsConditions', views.TermsConditions, name='TermsConditions'),
    path('product', views.Product, name='product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'app.views.custom_404_view'
