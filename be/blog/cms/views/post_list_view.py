from django.shortcuts import render
from cms.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'cms/post/list.html',
        {
            'posts': posts
        }
    )
