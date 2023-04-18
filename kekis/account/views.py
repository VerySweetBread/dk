from django.shortcuts import render
from .models import Account

def main(request,pk):
    account = Account.objects.get(name=pk)
    context = {'account':account}
    return render(request,'account/account.html', context)