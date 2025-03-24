from django.shortcuts import render, get_object_or_404,redirect
from .models import Cart
from products.models import Product

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect('cart_view')
