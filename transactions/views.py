from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FlashTransaction
from django.utils import timezone
from datetime import timedelta


def create_flash_transaction(request):
    if request.method == 'POST':
        user = request.user
        token_type = request.POST['token_type']
        amount = request.POST['amount']
        duration_days = int(request.POST['duration_days'])

        expiry_date = timezone.now() + timedelta(days=duration_days)
        transaction = FlashTransaction.objects.create(
            user=user,
            token_type=token_type,
            amount=amount,
            expiry_date=expiry_date
        )

        # Simulate blockchain interaction and return a response
        return JsonResponse({'status': 'success', 'transaction_id': transaction.id})

    return render(request, 'create_transactions.html')
