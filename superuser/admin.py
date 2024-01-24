from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Superuser)
class SuperuserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "email",
        "created_at",
    ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "fee", "created_at"]


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = [
        "start_dt",
        "timing",
        "created_at",
    ]


@admin.register(CrsLrn)
class CrsLrnAdmin(admin.ModelAdmin):
    list_display = [
        "course",
        "lrn_nm",
        "lrn_dsc",
        "created_at",
    ]
