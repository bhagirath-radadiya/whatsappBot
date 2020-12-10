from django.contrib import admin

# Register your models here.

from .models import Chat
from .models import File

admin.site.register(Chat)
admin.site.register(File)
