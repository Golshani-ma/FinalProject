from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from news.models import Post


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date

    def location(self, item):
        return reverse('news:news_single', kwargs={'pid': item.id})
