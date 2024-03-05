from django.shortcuts import render, get_object_or_404
from cms.models import Post
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.views.generic import ListView
from taggit.models import Tag


def post_list(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
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
            'posts': posts,
            'tag': tag,
        }
    )


class PostListView(ListView):
    """Alternative post list view"""
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "cms/post/list.html"
