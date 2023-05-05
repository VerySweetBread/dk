from django.shortcuts import render, redirect
from .models import Project, Contacts, Image, Account
from django.db.models import Q
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login

def home(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(Q(name__iregex=q) | Q(description__iregex=q) | Q(kvantum__icontains=q))
    context = {'projects': projects, 'account': account}
    return render(request, 'base/home.html', context)


def project(request, pk):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    project = Project.objects.get(id=pk)
    contacts = Contacts.objects.all()
    images = Image.objects.all()
    context = {'project': project,
               'contacts': contacts,
               'images': images,
               'account': account}
    return render(request, 'base/project.html', context)

def product(request, pk):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    shop = Shop.objects.get(id=pk)
    contacts = Contacts.objects.all()
    images = Image.objects.all()
    context = {'shop': shop,
               'contacts': contacts,
               'images': images,
               'account': account}
    print(images[0].image.url)
    return render(request, 'base/product.html', context)

def account(request, pk):
    account = Account.objects.get(id=pk)
    context = {'account': account}
    return render(request, 'base/account.html', context)

def login(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        response = redirect(f'/account/{id_per}/')
        return response
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                usr_account = Account.objects.get(login=cd["login"])
            except Account.DoesNotExist:
                print("Error")
                return redirect('/login/')
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                response = redirect(f'/account/{id_usr}/')
                return response
            else:
                print("Error")

        else:
            print("Error")
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})
    

def kvantum(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    q = request.GET.get('q')
    projects = Project.objects.filter(kvantum__icontains=q)
    context = {'projects': projects, 'account': account}
    return render(request, 'base/kvantum.html', context)

def rating(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    rank  = Account.objects.all().order_by("-rank")
    context = {'person': rank, "account": account}
    return render(request, 'base/rating.html', context)

def shop(request):
    if "id" in request.session:
        id_per = int(request.session['id'])
    else:
        id_per = 2
    account = Account.objects.get(id=id_per)
    shop = Shop.objects.all().order_by("-price")
    context = {'account': account, "shop": shop}
    return render(request, 'base/shop.html', context)

