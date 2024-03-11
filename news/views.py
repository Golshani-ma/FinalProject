from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from news.forms import CommentForm
from news.models import Post, Comment


# Create your views here.
# def news_single(request, pid):
#     current_datetime = timezone.now()
#
#     post = get_object_or_404(Post, id=pid, status=1)  # , published_date__lte=current_datetime)
#     context = {'post': post}
#     return render(request, 'news/single.html', context)

def news_single(request, pid):
    if request.method == 'POST':

        form = CommentForm(request.POST)
        # form.instance.post_id = pid
        print(form.instance.post_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'کامنت  شما با موفقیت ثبت شد.')
        else:
            messages.error(request, 'متاسفانه کامنت شما ثبت نشد.')

    try:
        current_datetime = timezone.now()
        #  Chapter 6 - Part 1 Excersice
        post = get_object_or_404(Post, id=pid, status=1, published_date__lte=current_datetime)
        if request.method == 'GET':
            post.counted_views += 1
            post.save()

        #  Chapter 6-Part 2 Excersice
        lst_post = list(
            Post.objects.filter(status=1, published_date__lte=current_datetime).order_by('-published_date'))
        post_index = lst_post.index(post)
        if post_index > 0:
            prev_post = lst_post[post_index - 1]
        else:
            prev_post = None

        if post_index == len(lst_post) - 1:
            next_post = None
        else:
            next_post = lst_post[post_index + 1]
        if post.login_required:
            if request.user.is_authenticated:
                comments = Comment.objects.filter(post=post.id, approved=True).order_by('-create_date')
                form = CommentForm()
                context = {'post': post, 'prev_post': prev_post, 'next_post': next_post, 'comments': comments,
                           'form': form}
                return render(request, 'news/single.html', context)
            else:
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            comments = Comment.objects.filter(post=post.id, approved=True).order_by('-create_date')
            form = CommentForm()
            context = {'post': post, 'prev_post': prev_post, 'next_post': next_post, 'comments': comments,
                       'form': form}
            return render(request, 'news/single.html', context)
    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")


def news_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts_total': posts}
    return render(request, 'website/index.html', context)
