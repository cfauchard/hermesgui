from django.contrib import admin

# Register your models here.

from .models import Connection
from .models import Permission

admin.site.register(Connection)
admin.site.register(Permission)