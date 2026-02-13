from django.contrib import admin
from .models import Student 
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display=('name', 'email', 'age', 'marks')
    search_fields=('name','email')

admin.site.register(Student , studentadmin)