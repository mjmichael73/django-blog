from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank
)
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
            search_vector = SearchVector('title', 'body')
            # search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            # search_vector = SearchVector('title', 'body', config='spanish')
            search_query = SearchQuery(query)
            # search_query = SearchQuery(query, config='spanish')
            search_rank = SearchRank(search_vector, search_query)
            # results = Post.published.annotate(
            #     search=search_vector,
            #     rank=search_rank,
            # ).filter(search=search_query).order_by('-rank')
            results = Post.published.annotate(
                search=search_vector,
                rank=search_rank,
            ).filter(search=search_query).order_by('-rank')
    return render(
        request,
        'cms/post/search.html',
        {
            'form': form,
            'query': query,
            'results': results
        }
    )
