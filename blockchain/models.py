from django.db import models

class BlockchainNetwork(models.Model):
    name = models.CharField(max_length=20)
    rpc_url = models.URLField()

class TransactionLog(models.Model):
    transaction_id = models.CharField(max_length=64)
    network = models.ForeignKey(BlockchainNetwork, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
