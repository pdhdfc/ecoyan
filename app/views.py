from django.utils.translation import gettext_lazy as _
from .forms import *
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

# def contact(request):
#     return render(request, 'contact.html')

def why_ecoyan(request):
    return render(request, 'why-ecoyan.html')

def certification(request):
    return render(request, 'certification.html')

def customers(request):
    return render(request, 'customers.html')

def photos(request):
    return render(request, 'photos.html')

def e_rickshaw(request):
    return render(request, 'e-rickshaw.html')


def e_cargo(request):
    return render(request, 'e-cargo.html')

def e_garbage(request):
    return render(request, 'e-garbage.html')

def golf_cart(request):
    return render(request, 'golf-cart.html')

def car(request):
    return render(request, 'car.html')





def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        try:
            ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
            return redirect('success')  # Redirect to success page
        except:
            return JsonResponse({'success': False})
    return render(request, 'contact.html') 

def dealer(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        try:
            ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
            return redirect('success')  # Redirect to success page
        except:
            return JsonResponse({'success': False})
    return render(request, 'dealer.html') 



def book_test_ride(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        state = request.POST.get('State')
        city = request.POST.get('City')
        purpose = request.POST.get('Purpose')
        message = request.POST.get('Message')

        try:
            BookTestRode.objects.create(
                name=name,
                email=email,
                phone=phone,
                state=state,
                city=city,
                purpose=purpose,  # Make sure to include purpose here
                message=message
            )
            return redirect('success')  # Redirect to success page
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'book_test_ride.html')




def success_view(request):
    return render(request, 'success.html')




def custom_404_view(request, exception):
    return render(request, '404.html', status=404)





from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta

def blogs(request):
    # Get all blog posts and order them by click_count in descending order
    blog_posts = BlogPost.objects.order_by('-click_count', '-date')

    # Define the time frame for trending posts (e.g., 7 days)
    trending_time_frame = timezone.now() - timedelta(days=7)

    # Separate trending and new posts based on click count and date
    trending_posts = [post for post in blog_posts if post.click_count >= 100 and post.date >= trending_time_frame]
    new_posts = [post for post in blog_posts if post not in trending_posts]

    posts_per_page = 5

    # Pagination for trending posts
    trending_paginator = Paginator(trending_posts, posts_per_page)
    trending_page = request.GET.get('trending_page')

    try:
        trending_posts_page = trending_paginator.page(trending_page)
    except PageNotAnInteger:
        trending_posts_page = trending_paginator.page(1)
    except EmptyPage:
        trending_posts_page = trending_paginator.page(trending_paginator.num_pages)

    # Pagination for new posts
    new_paginator = Paginator(new_posts, posts_per_page)
    new_page = request.GET.get('new_page')

    try:
        new_posts_page = new_paginator.page(new_page)
    except PageNotAnInteger:
        new_posts_page = new_paginator.page(1)
    except EmptyPage:
        new_posts_page = new_paginator.page(new_paginator.num_pages)

    context = {
        'include_main_css': False,
        'trending_posts_page': trending_posts_page,
        'new_posts_page': new_posts_page,
    }

    return render(request, 'blogs.html', context)

def blogs_details(request, slug):  # Change post_id to slug
    # Get the blog post based on its slug
    blog_post = get_object_or_404(BlogPost, slug=slug)

    # Increment click count
    blog_post.click_count += 1
    blog_post.save()

    context = {
        "blog_post": blog_post,
    }

    return render(request, 'blog_detalils.html', context)









def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'careers.html', {'jobs': jobs})



def job_detail(request, slug):
    try:
        job = get_object_or_404(Job, slug=slug)
    except Job.DoesNotExist:
        job = None
    return render(request, 'job_detail.html', {'job': job})


# def apply_for_job(request, pk):
#     job = get_object_or_404(Job, pk=pk)
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             application = form.save(commit=False)
#             application.job = job
#             application.save()
#             return redirect('job_detail', pk=job.pk)
#     else:
#         form = ApplicationForm()
#     return render(request, 'apply_for_job.html', {'form': form, 'job': job})


def apply_for_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    if not job.is_open:
        return render(request, 'job_closed.html', {'job': job})
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('job_detail', slug=job.slug)
    else:
        form = ApplicationForm()
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})


def PrivacyPolicy(request):
    return render(request, 'PrivacyPolicy.html')

def TermsConditions(request):
    return render(request, 'Terms&Conditions.html')

def Product(request):
    return render(request, 'product.html')