from django.urls import path
from .views import *


app_name = "order"



urlpatterns = [
    
    path('checkout', checkoutView.as_view(), name="checkout" ),

  
]