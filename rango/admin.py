from django.contrib import admin
from rango.models import Category,Page
from admin.ModelAdmin import admin.ModelAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, pageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class pageAdmin():
    list_display = ('title', 'category', 'url')