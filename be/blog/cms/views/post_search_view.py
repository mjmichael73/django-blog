from django.contrib.postgres.search import SearchVector
from cms.forms import SearchForm
from cms.models import Post
from django.shortcuts import render


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(
        request,
        'cms/post/search.html',
        {
            'form': form,
            'query': query,
            'results': results
        }
    )
