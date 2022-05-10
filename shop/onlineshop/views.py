from distutils.sysconfig import customize_compiler
from itertools import product
import json
from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import *

####################################
def onlineshop(request):
    data=cartData(request)
    cartItems=data["cartItems"]

    products=Product.objects.all()
    context = {"products":products,"cartItems":cartItems}
    return render(request,'onlineshop/home.html',context)

####################################
def mycart(request):
    data=cartData(request)
    cartItems=data["cartItems"]
    order=data["order"]
    items=data["items"]
                
    context = {"items":items,"order":order,"cartItems":cartItems,}
    return render(request,'onlineshop/mycart.html',context)

########################################
def proceed(request):
    data=cartData(request)
    cartItems=data["cartItems"]
    order=data["order"]
    items=data["items"]

    context = {"items":items,"order":order,"cartItems":cartItems,}
    return render(request,'onlineshop/proceed.html',context)

#######################################
def updateItem(request):
    data= json.loads(request.body)
    productId=data["productId"]
    action=data["action"]
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,completed=False)
    orderitem,created= OrderItem.objects.get_or_create(order=order,product=product)
    if action=="add":
        orderitem.quantity = (orderitem.quantity+1)
    elif action=="remove":
        orderitem.quantity = (orderitem.quantity-1)
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse("Item was added" , safe=False)


#######################################
def paymentProcess(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,completed=False)
    else:
        customer,order=guestCart(request,data)

    total=float(data["userFormData"]["total"])
    order.transaction_id=transaction_id
    print(total)
    if total==order.get_cart_total:
        order.completed=True
    order.save()
    if order.shipping_check==True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data["shippingData"]["address"],
            city=data["shippingData"]["city"],
            state=data["shippingData"]["state"],
            pincode=data["shippingData"]["pincode"],
        )

    return JsonResponse("Payment complete" , safe=False)

#########################################
def logout(request):
    auth.logout(request)
    return redirect('/')