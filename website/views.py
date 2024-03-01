from django.shortcuts import render
from news.models import Post


# Create your views here.
def home_view(request):
    posts_rotated = list(Post.objects.filter(status=1))[:3]
    posts_static = list(Post.objects.filter(status=1))[3:7]

    context = {'posts_rotated': posts_rotated, 'posts_static': posts_static}
    # context = {'posts_rotated': posts_rotated}
    return render(request, 'website/index.html', context)


def contact_view(request):
    return render(request, 'website/contact.html')
