from django.contrib import admin

from .models import Rezervace,Zakaznik,Pokoj

# Register your models here.

admin.site.register(Rezervace)
admin.site.register(Zakaznik)
admin.site.register(Pokoj)
