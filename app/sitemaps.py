from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import BlogPost
from .models import Job
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
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date

class JobDetailSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.title
