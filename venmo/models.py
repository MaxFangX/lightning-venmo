from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from venmo.fields import BitcoinAddressField


class Profile(models.Model):
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    handle = models.CharField(max_length=30)
    lightning_address = BitcoinAddressField()


class Payment(models.Model):

    PAYMENT_STATUS_CHOICES = (
        ('pending_invoice', 'Pending Invoice'),
        ('pending_payment', 'Pending Payment'),
        ('complete', 'Complete'),
    )
    status = models.CharField(max_length=50, default='accepted', choices=PAYMENT_STATUS_CHOICES)

    sender = models.ForeignKey(User)
    recipient = models.ForeignKey(User)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default='accepted', choices=PAYMENT_STATUS_CHOICES)

admin.site.register(Profile)
admin.site.register(Payment)
