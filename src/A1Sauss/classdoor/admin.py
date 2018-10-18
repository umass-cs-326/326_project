from django.contrib import admin
from classdoor.models import ClassDesc

# Register your models here.

@admin.register(ClassDesc)
class ClassDescAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "description", "rating")
    fields = ["name", "teacher", "description", "rating"]
