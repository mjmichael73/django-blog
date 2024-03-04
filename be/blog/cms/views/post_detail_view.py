from django.http import Http404
from cms.models import Post, Comment
from django.shortcuts import render, get_object_or_404
from cms.forms import CommentForm


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(
        request,
        'cms/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form
        }
    )
