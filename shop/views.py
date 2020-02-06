from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from . import models
from cart.forms import CartAddProductForm
from cart.cart import Cart
from decimal import Decimal


def index(request):
    product_list = models.Product.objects.all()[:5]
    return render(request, 'index.html', {'product_list': product_list})


@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = models.Order.objects.create(customer=request.user)
        for item in cart:
            models.OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            product_price=item['price'],
                                            product_count=item['product_count'],
                                            product_cost=Decimal(item['product_count']) * Decimal(item['price']))
        # order.customer = request.user
        # order.save()
        cart.clear()
        return render(request, 'order_detail.html', {'order': order})
    return render(request, 'checkout.html', {'cart': cart})


def product(request, pk):
    product_detail = get_object_or_404(models.Product, id=pk)
    cart_add_product_form = CartAddProductForm()
    return render(request, 'product.html', {'product_detail': product_detail,
                                            'cart_add_product_form': cart_add_product_form})


def store(request):
    return render(request, 'store.html')
