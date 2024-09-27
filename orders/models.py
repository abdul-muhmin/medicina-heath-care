from django.db import models
from customers.models import Customer
from production.models import Product
# Create your models here.


class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Customer ,on_delete=models.SET_NULL, null=True,related_name='orders')
    CART_STAGE=0
    ORDER_CONFORMED=1
    ORDER_REJECTED=4
    ORDER_PROSSED=2
    ORDER_DELEVERED=3
    STATUS_CHOICE=((ORDER_PROSSED,"ORDER_PROSSED"),
                   (ORDER_DELEVERED,"ORDER_DELEVERED"),
                   (ORDER_REJECTED,"ORDER_REJECTED"),
                   (ORDER_CONFORMED,"ORDER_CONFORMED")
                   )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    total_price=models.FloatField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.name)
    
class OrderedItem(models.Model):
    product=models.ForeignKey(Product, related_name='added_carts',on_delete=models.SET_NULL, null= True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')
    