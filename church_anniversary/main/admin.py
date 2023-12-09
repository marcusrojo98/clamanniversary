from django.contrib import admin

# Register your models here.
# main/admin.py
from .models import Photo

admin.site.register(Photo)
