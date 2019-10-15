from django.db import models
from usermanagement.models import User
from listings.models import Listings
from categories.models import Categories
from coupons.models import Coupons

# Create your models here.
class Payments(models.Model):
    user_id =models.ForeignKey(User , on_delete=models.CASCADE)
    listing_id=models.ForeignKey(Listings, on_delete=models.CASCADE)
    categorie_id=models.ForeignKey(Categories , on_delete=models.CASCADE)
    coupons_id=models.ForeignKey(Coupons,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=5, decimal_places=2)
    payment_mdoe=models.CharField(max_length=40)
    status=models.CharField(max_length=20)
    transaction_id=models.CharField(max_length=20
                                    )