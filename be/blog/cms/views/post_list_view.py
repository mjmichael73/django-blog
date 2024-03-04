from django.shortcuts import render
from cms.models import Post
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.views.generic import ListView


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'cms/post/list.html',
        {
            'posts': posts
        }
    )


class PostListView(ListView):
    """Alternative post list view"""
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "cms/post/list.html"
