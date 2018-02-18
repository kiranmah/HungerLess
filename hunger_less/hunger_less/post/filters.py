import django_filters
from .models import post, postlink,foodtype
from hunger_less.users.models import User
from django_filters.widgets import RangeWidget
from django import forms

class PostFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(label='Company', 
    queryset=User.objects.all()
    )
    foodtype = django_filters.ModelChoiceFilter(label='Food', 
    queryset=foodtype.objects.all(),
    to_field_name='name'
    )
    date = django_filters.DateFilter(label='Submission Date',lookup_expr='date__gte')
    collectdate = django_filters.DateFilter(label='Collection Deadline',lookup_expr='date__lte')

    class Meta:
        model = post
        fields = {}