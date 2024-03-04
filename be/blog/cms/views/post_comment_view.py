from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from cms.models import Post, Comment
from cms.forms import CommentForm


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(
        request,
        "cms/post/comment.html",
        {
            "post": post,
            "form": form,
            "comment": comment
        }
    )
