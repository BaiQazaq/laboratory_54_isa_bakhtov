from django.contrib import admin

from shop_app.models import Category, Good

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "created_at")
    list_filter = ("id", "title", "description", "created_at")
    search_fields = ("title", "description")
    fields = ("title", "description", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Category, CategoryAdmin)

class GoodAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "price", "photo", "category", "created_at")
    list_filter = ("id", "title", "description", "price", "category", "created_at")
    search_fields = ("title", "description")
    fields = ("title", "description", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Good, CategoryAdmin)

