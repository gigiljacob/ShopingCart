from django.db import models

from accounts.models import User


class SellerInformation(models.Model):
    """
    Information about the seller
    """
    categories = (
        ('cat1', 'Textiles'),('cat2', 'General Store')
    )

    store_name = models.CharField(max_length=100, null=False, blank=False)
    main_category = models.CharField(max_length=40, choices=categories, null=False, blank=False)
    address1 = models.CharField(max_length=155, null=False, blank=False)
    address2 = models.CharField(max_length=155, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    pin_code = models.PositiveIntegerField(null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)

    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.store_name


class TaxInformation(models.Model):
    """
    Tax information for the store
    """
    provisional_gstin = models.CharField(max_length=100, null=True, blank=True)
    pan_number = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, models.CASCADE)
    seller_info = models.ForeignKey(SellerInformation, models.CASCADE)

    def __str__(self):
        return self.provisional_gstin + self.pan_number

