from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from news.models import Post


# Create your views here.
def news_single(request, pid):
    current_datetime = timezone.now()

    post = get_object_or_404(Post, id=pid, status=1)  # , published_date__lte=current_datetime)
    context = {'post': post}
    return render(request, 'news/single.html', context)
