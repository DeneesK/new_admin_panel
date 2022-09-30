from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView

from movies.models import Filmwork


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        pre_q = Filmwork.objects.annotate(
            genres=ArrayAgg('genre__name', distinct=True),
            actors=ArrayAgg('person__full_name',
                            filter=Q(personfilmwork__role='actor'),
                            distinct=True),
            directors=ArrayAgg('person__full_name',
                               filter=Q(personfilmwork__role='director'),
                               distinct=True),
            writers=ArrayAgg('person__full_name',
                             filter=Q(personfilmwork__role='writer'),
                             distinct=True)
            )
        queryset = pre_q.values(
            'id', 'title', 'description', 'creation_date', 'rating',
            'type', 'genres', 'actors', 'directors', 'writers'
        )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, _ = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        prev = page.previous_page_number() if page.has_previous() else None
        next_ = page.next_page_number() if page.has_next() else None
        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': prev,
            'next': next_,
            'results': list(queryset)
        }


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        context = kwargs['object']
        return context
