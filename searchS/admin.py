# admin.py
from django.contrib import admin
from .models import Hospital
from .models import Medicine


admin.site.register(Hospital)
admin.site.register(Medicine)

