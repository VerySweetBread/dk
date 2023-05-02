from django.shortcuts import render, redirect
from .models import Project, Contacts, Image, Account
from django.db.models import Q
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
from django_pushall import Pushall

def home(request):
    id_per = int(request.session['id'])
    account = Account.objects.get(id=id_per)
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
    if 'id' in request.session:
        id_per = int(request.session['id'])
        response = redirect(f'/account/{id_per}/')
        return response
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usr_account = Account.objects.get(login=cd["login"])
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                response = redirect(f'/account/{id_usr}/')
                return response
            else:
                Pushall.self(title="Ploxoy otvet", text = "lapux")

        else:
            Pushall.self(title="Ploxoy adad", text = "asdada")
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})
    

def kvantum(request):
    account = Account.objects.get(id=1)
    q = request.GET.get('q')
    projects = Project.objects.filter(kvantum__icontains=q)
    context = {'projects': projects, 'account': account}
    return render(request, 'base/kvantum.html', context)


def about(request):
    return render(request, 'base/about.html')

def shop(request):
    return render(request, 'base/about.html')
