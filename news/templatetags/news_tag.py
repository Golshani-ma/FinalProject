from django import template
from django.utils import timezone
from news.models import Post, Category,Comment

register = template.Library()


@register.simple_tag(name="comment_count")
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()


@register.simple_tag
def post_titles():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet_func(value, arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('news/populernews.html')
def popular_news(num=5):
    posts = Post.objects.filter(status=1).order_by('-counted_views')[:num]
    return {'posts': posts}


@register.inclusion_tag('news/last_news.html')
def latest_post_down(num=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:num]
    return {'posts': posts}




@register.inclusion_tag('news/category_tag.html')
def news_post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat_name in categories:
        cat_dict[cat_name.name] = posts.filter(category=cat_name).count()

    return {'categories': cat_dict}

@register.inclusion_tag('news/category_tag_side.html')
def news_post_categories_side():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat_name in categories:
        cat_dict[cat_name.name] = posts.filter(category=cat_name).count()

    return {'categories': cat_dict}


# @register.inclusion_tag('website/website-latest-posts.html')
# def latest_post_bottom(num=6):
#     '''
#     Capter 7 Exersice Template Tag
#     '''
#     current_time = timezone.now()
#     posts = Post.objects.filter(status=1, published_date__lte=current_time).order_by('-published_date')[:num]
#
#     return {'posts': posts}
