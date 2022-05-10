import json
from .models import *

#######################################
def cookieCart(request):
    try:
            cart = json.loads(request.COOKIES["cart"])
    except:
            cart={}
    items=[]
    order={"get_cart_total":0,"get_quantity":0,"shipping_check":False,}
    cartItems=order["get_quantity"]

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])

            order["get_cart_total"] += total
            order["get_quantity"] += cart[i]["quantity"]

            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "image": product.image,
                },
                "quantity": cart[i]["quantity"],
                "get_total": total,
            }
            items.append(item)

            if product.digital == False:
                order["shipping_check"] = True
        except:
            pass
    return {"cartItems":cartItems ,"order":order, "items":items}


######################################
def cartData(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,completed=False)
        items=order.orderitem_set.all()
        cartItems=order.get_quantity
    else:
        cookieData=cookieCart(request)
        cartItems=cookieData["cartItems"]
        order=cookieData["order"]
        items=cookieData["items"]
    return {"cartItems":cartItems ,"order":order, "items":items}


#######################################
def guestCart(request,data):
    print("user is not logged in")
    print("COOKIES:",request.COOKIES)
    name=data["userFormData"]["name"]
    email=data["userFormData"]["email"]

    cookieData= cookieCart(request)
    items=cookieData["items"]

    customer, created= Customer.objects.get_or_create(email=email,)
    customer.name=name
    customer.save()

    order=Order.objects.create(
        customer=customer,
        completed=False,
    )
    for item in items:
        product=Product.objects.get(id=item["product"]["id"])

        oderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item["quantity"],
        )
    return customer,order