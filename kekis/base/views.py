from django.shortcuts import render, redirect
from .models import Project, Contacts, Image, Account
from django.db.models import Q
from django.http import HttpResponse
from .forms import *

def home(request):
    account = Account.objects.get(id=1)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(Q(name__iregex=q) | Q(description__iregex=q) | Q(kvantum__icontains=q))
    context = {'projects': projects, 'account': account}
    return render(request, 'base/home.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    contacts = Contacts.objects.all()
    images = Image.objects.all()
    context = {'project': project,
               'contacts': contacts,
               'images': images}
    return render(request, 'base/project.html', context)


def account(request, pk):
    account = Account.objects.get(id=pk)
    context = {'account': account}
    return render(request, 'base/account.html', context)


def login(request):
    form_login = LoginForm() 
    context = {'form': form_login}
    if 'id' in request.session:
        id_per = int(request.session['id'])
        response = redirect(f'/account/{id_per}/')
        return response
    else:
        """request.session.set_expiry(10)
        request.session['id'] = 1"""
        return render(request, 'base/login.html', context)
    
    
    

def kvantum(request):
    account = Account.objects.get(id=1)
    q = request.GET.get('q')
    projects = Project.objects.filter(kvantum__icontains=q)
    context = {'projects': projects, 'account': account}
    return render(request, 'base/kvantum.html', context)


def about(request):
    return render(request, 'base/about.html')
