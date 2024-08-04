from django.db import models
from django.conf import settings

class FlashTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token_type = models.CharField(max_length=10)  # e.g., USDT, BTC, TRX
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=10, default='pending')  # pending, confirmed, expired
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()