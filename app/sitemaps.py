from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'index', 'about', 'contact', 'dealer', 'book_test_ride',
            'photos', 'e_rickshaw', 'e_cargo', 'e_garbage',
            'golf_cart', 'blogs', 'job_list', 'PrivacyPolicy', 'TermsConditions', 'product'
        ]

    def location(self, item):
        return reverse(item)

class BlogPostSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date

class JobDetailSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # Use the created_at field from the Job model

class DynamicUrlSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return DynamicURL.objects.all()

    def lastmod(self, obj):
        return obj.created_at