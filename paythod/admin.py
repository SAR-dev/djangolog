from django.contrib import admin
from .models import Paythod

@admin.register(Paythod)
class PaythodAdmin(admin.ModelAdmin):
    pass