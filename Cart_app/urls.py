from django.urls import path,include
from .views import cart_detail,cart_add,cart_remove

app_name = 'Cart_app'

urlpatterns = [
    path('',cart_detail,name='cartdetail'),
    path('add/<int:product_id>',cart_add,name='cartadd'),
    path('remove/<int:product_id>',cart_remove,name='cartremove'),
]
