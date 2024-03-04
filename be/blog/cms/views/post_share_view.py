from cms.forms import EmailPostForm
from django.shortcuts import get_object_or_404, render
from cms.models import Post


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if not form.is_valid():
            form = EmailPostForm()
        else:
            cd = form.cleaned_data
            # TODO Send Email
    return render(
        request,
        "cms/post/share.html",
        {
            "post": post,
            "form": form
        }
    )
