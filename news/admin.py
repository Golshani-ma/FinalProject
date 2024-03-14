from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from news.models import Post, Category, Comment


# class PostAdmin(SummernoteModelAdmin):
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # list_display = ['pk', 'title', 'author', 'image', 'counted_views', 'login_required', 'status', 'published_date',
    #                 'created_date']
    list_display = ['pk', 'title', 'author', 'counted_views', 'login_required', 'status', 'published_date',
                    'created_date']
    list_filter = ['status', 'author']

    search_fields = ['title', 'counted_views', 'status', 'published_date', 'created_date']
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = '-empty-'
    list_display = ['name', 'post', 'approved', 'create_date']
    list_filter = ['name', 'post', 'approved']
    search_fields = ['post', 'name', 'create_date']
    summernote_fields = ('content',)


admin.site.register(Comment, CommentAdmin)
