from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

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




