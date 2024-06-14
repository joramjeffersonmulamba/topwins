from django.contrib import admin
from .models import category

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
admin.site.register(category, categoryAdmin)