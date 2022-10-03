from django.shortcuts import render
from django.views.generic import  CreateView
from . models import  Order
from .forms import OrderForm
from cart.models import Cart

# Create your views here.

class checkoutView(CreateView):
    model = Cart
    form_class = OrderForm
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.all()
        context['cart'] = cart
        return context
