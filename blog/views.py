from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import Post

def post_list(request):
    posts = Post.published.filter(status='published')

    paginator = Paginator(posts, 3) # 5 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {
        'posts': posts,
        page: 'pages'
        })

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'post': post})

