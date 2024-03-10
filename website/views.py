from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from news.models import Post
from website.forms import ContactForm, NewsletterForm


# Create your views here.
# def home_view(request):
#     posts_rotated = list(Post.objects.filter(status=1))[:3]
#     posts_static = list(Post.objects.filter(status=1))[3:7]
#     posts_total = list(Post.objects.filter(status=1))[7:]
#
#     context = {'posts_rotated': posts_rotated, 'posts_static': posts_static, 'posts_total': posts_total}
#     # context = {'posts_rotated': posts_rotated}
#     return render(request, 'website/index.html', context)


def home_view(request, **kwargs):
    current_datetime = timezone.now()

    posts_rotated = (Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date'))
    posts_static = (Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date'))
    posts_total = (Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date'))

    if kwargs.get('cat_name') is not None:
        posts_rotated = posts_rotated.filter(category__name=kwargs['cat_name'])
        posts_static = posts_static.filter(category__name=kwargs['cat_name'])
        posts_total = posts_total.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts_rotated = posts_rotated.filter(author__username=kwargs['author_username'])
        posts_static = posts_static.filter(author__username=kwargs['author_username'])
        posts_total = posts_total.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts_rotated = posts_rotated.filter(tags__name__in=[kwargs['tag_name']])
        posts_static = posts_static.filter(tags__name__in=[kwargs['tag_name']])
        posts_total = posts_total.filter(tags__name__in=[kwargs['tag_name']])
    try:
        posts_total = Paginator(posts_total, 6)
        page_number = request.GET.get("page")
        posts_total = posts_total.get_page(page_number)
    except PageNotAnInteger:
        posts_total = posts_total.get_page(1)
    except EmptyPage:
        posts_total = posts_total.get_page(posts_total.num_pages)

    posts_rotated = list(posts_rotated)[:3]
    posts_static = list(posts_static)[3:7]
    # posts_total = list(posts_total)[7:]

    context = {'posts_rotated': posts_rotated, 'posts_static': posts_static, 'posts_total': posts_total}

    return render(request, 'website/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'اطلاعات شما با موفقیت ثبت شد.')
        else:
            messages.error(request, 'متاسفانه خطایی پیش آمده. مجددا امتحان کنید.')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
