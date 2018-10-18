from django.contrib import admin
# Register your models here.
from .models import Events
from .models import Pet

admin.site.register(Events)
admin.site.register(Pet)
