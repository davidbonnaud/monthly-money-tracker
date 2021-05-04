from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Balance,Transaction

def index(request):
	balance = Balance.objects.first()
	if(balance):
		transaction_list = Transaction.objects.order_by('-date_time')
		for transaction in transaction_list:
			balance.total += transaction.amount
		context = { 
			'transaction_list': transaction_list,
			'balance': balance,
		}
		return render(request, 'money/index.html', context)
	else:
		balance = Balance()
		balance.total = 0
		balance.save()

	
  
def add_transaction(request):
	if request.method=="POST":
		balance = Balance.objects.first()
		transaction = Transaction()
		transaction.balance = balance
		transaction.amount = request.POST.get('amount')
		transaction.details = request.POST.get('details')
		transaction.save()
		return redirect('/')
	else:
		return redirect('/')


#def delete_transaction(request, transaction_id):
  #transaction = get_object_or_404(Transaction, pk=transaction_id)