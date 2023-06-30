from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from app.models import Phone

# Create your views here.


def index(request):
    return render(request,"index.html")
#
# def sell(request):
#     return render(request,"sell.html")


def sell(request):
    if request.method == 'POST':
        name = request.POST['name']
        manufacturer = request.POST['manufacturer']
        color = request.POST['color']
        storage = request.POST['storage']
        used = 'used' in request.POST
        price = request.POST['price']
        owner = request.user
        image = request.FILES.get('image')
        location = request.FILES.get('location')

        phone = Phone(
            name=name,
            manufacturer=manufacturer,
            color=color,
            storage=storage,
            used=used,
            price=price,
            owner=owner,
            image=image,
            location=location
        )
        phone.save()
        return redirect('sellAdded')  # Redirect to a view displaying the list of phones

    return render(request, 'sell.html')



def sellAdded(request):
    return render(request,'AddingNewProduct.html')


def results(request):
    search_query = request.GET.get('search_query', '')
    used = request.GET.get('used', '')

    if search_query and used == 'on':
        # Both search_query contains the name of the phone and used is 'on'
        # Add your logic here to retrieve phones that contain the search_query and are used
        phones = Phone.objects.filter(name__icontains=search_query)
        context = {
            'phones': phones
        }
        return render(request, 'results.html', context)

    elif search_query:
        # Only search_query contains the name of the phone
        # Add your logic here to retrieve phones that contain the search_query and are not used
        phones = Phone.objects.filter(name__icontains=search_query, used=False)
        context = {
            'phones': phones
        }
        return render(request, 'results.html', context)

    elif used:
        # Only search_query contains the name of the phone
        # Add your logic here to retrieve phones that contain the search_query and are not used
        phones = Phone.objects.all()
        context = {
            'phones': phones
        }
        return render(request, 'results.html', context)

    else:
        # search_query is empty or None
        # Add your logic here to retrieve all phones
        phones = Phone.objects.filter(used=False)
        context = {"phones": phones}

        return render(request, 'results.html', context)



def phone_details(request, id):
    phone = get_object_or_404(Phone, id=id)
    previous_url = request.META.get('HTTP_REFERER')
    context = {
        'phone': phone,
        'previous_url': previous_url
    }
    return render(request, 'details.html', context)

def payment(request, id):
    phone = get_object_or_404(Phone, id=id)
    previous_url = request.META.get('HTTP_REFERER')
    context = {
        'phone': phone,
        'previous_url': previous_url
    }
    return render(request, 'payment.html', context)


def paymentDelivery(request, id):
    phone = get_object_or_404(Phone, id=id)
    previous_url = request.META.get('HTTP_REFERER')
    context = {
        'phone': phone,
        'previous_url': previous_url
    }
    return render(request, 'paymentDelivery.html', context)

def payed(request):
    return render(request, 'payed.html')


