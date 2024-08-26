from django.contrib import admin
from super.models import Category, Publication, HashTag

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    list_display = ['title', 'text', 'category', 'image']

@admin.register(HashTag)
class AdminHashTag(admin.ModelAdmin):
    list_display = ['hashtag_name']
