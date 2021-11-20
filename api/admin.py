from django.contrib import admin
from .models import Category , Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name' , 'title','description' ,'url')


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_filter = ('name',)
    list_per_page = 5

admin.site.register(Post, PostAdmin)
