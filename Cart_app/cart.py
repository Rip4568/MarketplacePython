from decimal import Decimal
import copy

from django.conf import settings
from Cart_app.forms import CartAddProductForm
from MarketplacePython.settings import CART_ITEM_MAX_QUANTITY

from Produtos_app.models import Product

class Cart:
    def __init__(self,request):
        if request.session.get("cart") is None:
            request.session["cart"] = {}

        self.cart = request.session['cart']
        self.session = request.session

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        products = Product.objects.filter(id__in=cart)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["quantity"] * item["price"]
            item["update_quantity_form"] = CartAddProductForm(
                initial={"quantity": item["quantity"], "override": True}
            )

            yield item
    
    def add(self,product,quantity=1,override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity":quantity,
                "price":str(product.price)
            }
        if override_quantity:
            #self.cart.product[product_id]["quantity"] = quantity
            self.cart[product_id]["quantity"] = quantity
        else:
            #self.cart.product[product_id]["quantity"] += quantity
            self.cart[product_id]["quantity"] += quantity
        
        self.cart[product_id]["quantity"] = min(CART_ITEM_MAX_QUANTITY,self.cart[product_id]["quantity"])
            
        self.save()
    
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        

    def get_total_price(self):
            return sum(
                Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
                )
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
        
    def save(self):
        self.session.modified = True