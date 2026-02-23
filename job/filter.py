import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    min_salary = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    max_salary = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    min_experience = django_filters.NumberFilter(field_name='experience', lookup_expr='gte')
    max_experience = django_filters.NumberFilter(field_name='experience', lookup_expr='lte')

    class Meta:
        model = Job
        fields = ['job_type', 'vacancy', 'category']
