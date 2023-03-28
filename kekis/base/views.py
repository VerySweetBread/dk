from django.shortcuts import render
from .models import Project, Contacts, Image
from django.db.models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(Q(name__iregex = q) | Q(description__iregex = q) | Q(kvantum__icontains = q))
    context = {'projects':projects}
    return render(request, 'base/home.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    contacts = Contacts.objects.all()
    images = Image.objects.all()
    context = {'project':project,
               'contacts':contacts,
               'images':images}
    return render(request, 'base/project.html', context)

def kvantum(request):
    q = request.GET.get('q')
    projects = Project.objects.filter(kvantum__icontains = q)
    context = {'projects':projects}
    return render(request, 'base/kvantum.html', context)

def about(request):
    return render(request, 'base/about.html')

