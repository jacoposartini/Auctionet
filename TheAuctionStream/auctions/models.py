from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    starting_price = models.PositiveIntegerField()
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name="own_products")

class Auction(Product):
    product_ptr = models.OneToOneField(Product,
                                    on_delete=models.CASCADE,
                                    primary_key=True)
    start_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    current_price = models.PositiveIntegerField()
    winner = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="won_auctions")

    def get_absolute_url(self):
        return "/%i/" % self.id

    def __str__(self):
        return self.name







locals
