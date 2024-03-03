from django.http import Http404
from cms.models import Post
from django.shortcuts import render


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No post found.")

    return render(
        request,
        'cms/post/detail.html',
        {
            'post': post
        }
    )
