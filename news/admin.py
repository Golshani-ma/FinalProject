from django.contrib import admin

# Register your models here.
from news.models import Post, Category


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
