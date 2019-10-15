from django.db import models
from usermanagement.models import User
from listings.models import Listings
from categories.models import Categories
class Coupons(models.Model):
    user_id=models.ForeignKey(User ,on_delete=models.CASCADE)
    listing_id=models.ForeignKey(Listings,on_delete=models.CASCADE)
    categorie_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    #categorie_id=models.Foreignkey(Categories,on_delete=models.CASCADE)
    coupon_code=models.CharField(max_length=20)
    immage=models.ImageField()
    start_date=models.DateField()
    end_date = models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()

