from django.shortcuts import render

def main(request,pk):
    return render(request,'account/account.html',{"name":pk})