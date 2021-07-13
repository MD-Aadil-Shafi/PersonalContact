from django.contrib import admin
from django.contrib.auth.models import Group

from . models import Contact,Message

# Register your models here.

admin.site.unregister(Group)
admin.site.register(Contact)
admin.site.register(Message)