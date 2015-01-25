
from django.contrib import admin
from rango.models import Category, Page,UserProfile

class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)