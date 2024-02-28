from django.shortcuts import render


# Create your views here.
def single_view(request):
    return render(request, 'news/single.html')