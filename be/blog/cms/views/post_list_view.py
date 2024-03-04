from django.shortcuts import render
from cms.models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(
        request,
        'cms/post/list.html',
        {
            'posts': posts
        }
    )
