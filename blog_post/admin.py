from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'created_on')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article,admin_class=ArticleAdmin)