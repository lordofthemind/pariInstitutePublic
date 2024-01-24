from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['fname', 'email', 'qualification', 'experties_1',]