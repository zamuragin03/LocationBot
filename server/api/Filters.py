from django_filters import rest_framework as filter
from api.models import UserAction

class CharFilterInFilter(filter.BaseInFilter, filter.CharFilter):
    ...

class  UserActionsFilter(filter.FilterSet):
    date = filter.DateRangeFilter(field_name = 'time')
    date_range = filter.DateTimeFromToRangeFilter(field_name='time')
    class Meta:
        model = UserAction
        fields = ('date',)