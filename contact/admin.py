from django.contrib import admin
from contact import models
# flake8: noqa

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone', 'email',
    ordering = '-id',
    search_fields = 'id' , 'first_name' , 'last_name' ,
    list_per_page = 10 
    list_max_show_all = 1000 
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id','phone', 
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',