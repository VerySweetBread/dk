from django.shortcuts import render
from .models import Account

def main(request,pk):
    account = Account.objects.get(name=pk)
    context = {'account':account}
<<<<<<< HEAD
    return render(request,'account/account.html', context)
=======
    return render(request,'account/account.html', context)
    
>>>>>>> 3977d66382862d63c2a04e4b105e41d7f87b28e0
