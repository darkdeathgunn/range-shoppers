from django import views
from django.urls import URLPattern, path

from .views import *

urlpatterns = [
    path('', onlineshop, name="onlineshop"),
    path('mycart/', mycart, name="mycart"),
    path('proceed/', proceed, name="proceed"),
    path('update_item/', updateItem, name="update_item"),
    path('payment_process/', paymentProcess, name="payment_process"),
    path('logout/', logout, name="logout"),
]