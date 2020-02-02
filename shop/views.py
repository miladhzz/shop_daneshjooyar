from django.shortcuts import render, get_object_or_404
from . import models
from cart.forms import CartAddProductForm


def index(request):
    product_list = models.Product.objects.all()[:5]
    return render(request, 'index.html', {'product_list': product_list})


def checkout(request):
    return render(request, 'checkout.html')


def product(request, pk):
    product_detail = get_object_or_404(models.Product, id=pk)
    cart_add_product_form = CartAddProductForm()
    return render(request, 'product.html', {'product_detail': product_detail,
                                            'cart_add_product_form': cart_add_product_form})


def store(request):
    return render(request, 'store.html')
