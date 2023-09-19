from django_filters import rest_framework as filter
from api.models import UserAction, TelegramUser

class CharFilterInFilter(filter.BaseInFilter, filter.CharFilter):
    ...

class  UserActionsFilter(filter.FilterSet):
    date = filter.DateRangeFilter(field_name = 'time')
    date_range = filter.DateTimeFromToRangeFilter(field_name='time')
    class Meta:
        model = UserAction
        fields = ('date',)

class  TelegramUserFilter(filter.FilterSet):
    is_notificated = filter.BooleanFilter(field_name ='is_notificated')
    class Meta:
        model = TelegramUser
        fields = ('is_notificated',)