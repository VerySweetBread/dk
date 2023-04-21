from django.contrib import admin
from .models import Image
from .models import Project
from .models import Contacts, Account


class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
admin.site.register(Contacts)
admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Account)