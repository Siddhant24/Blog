from django.contrib import admin

# Register your models here.

from .models import Blogger, Blogpost, Comment

class BlogpostInLine(admin.TabularInline):
    model = Blogpost
    extra = 0

class BloggerAdmin(admin.ModelAdmin):
	list_display = ('user','name', 'bio')
	inlines = [BlogpostInLine]

admin.site.register(Blogger, BloggerAdmin)

class CommentInLine(admin.TabularInline):
	model = Comment
	extra = 0

class BlogpostAdmin(admin.ModelAdmin):
	list_display = ('title','post_date','author','description')
	inlines = [CommentInLine]

admin.site.register(Blogpost, BlogpostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id','commenter', 'blogpost', 'post_date','post_time','description')

admin.site.register(Comment, CommentAdmin)