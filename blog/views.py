from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post

from django.conf import settings


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, settings.MAX_POSTS_PER_PAGE)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
         posts = paginator.page(1)
    except EmptyPage:
            posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'posts': posts})
