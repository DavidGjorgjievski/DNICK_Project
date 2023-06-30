"""Hotphone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, sell, sellAdded, results, phone_details,payment,paymentDelivery, payed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('sell/', sell, name="sell"),
    path('sell/added/', sellAdded, name="sellAdded"),
    path('results/', results, name="results"),
    path('details/<int:id>/', phone_details, name="phone_details"),
    path('payment/<int:id>/', payment, name="payment"),
    path('payment/delivery/<int:id>/', paymentDelivery, name="paymentDelivery"),
    path('payed/', payed, name="payed"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
