from django.shortcuts import render

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



from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage

from django.shortcuts import redirect

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

def success_view(request):
    return render(request, 'success.html')


from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
