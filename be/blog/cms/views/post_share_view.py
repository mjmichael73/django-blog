from cms.forms import EmailPostForm
from django.shortcuts import get_object_or_404, render
from cms.models import Post
from django.core.mail import send_mail


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if not form.is_valid():
            form = EmailPostForm()
        else:
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(
                subject,
                message,
                'test@example.com',
                [cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        "cms/post/share.html",
        {
            "post": post,
            "form": form,
            'sent': sent,
        }
    )
