from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .Filters import UserActionsFilter, TelegramUserFilter
class TelegramUserBaseModel:
    serializer_class = TelegramUserSerializer
    queryset = TelegramUser.objects.all()

class LocationBaseModel:
    serializer_class = LocationsSerializer
    queryset = Location.objects.all()

class UserActionBaseModel:
    serializer_class = UserActionSerializer
    queryset = UserAction.objects.all()

class ActionTypeBaseModel:
    serializer_class = ActionTypeSerializer
    queryset = ActionType.objects.all()


class CreateTelegramUser(TelegramUserBaseModel, generics.CreateAPIView):
    ...

class GetTelegramUser(TelegramUserBaseModel, generics.RetrieveAPIView):
    lookup_field='external_id'

class UpdateTelegramUser(TelegramUserBaseModel, generics.RetrieveUpdateAPIView):
    lookup_field='external_id'

class GetTelegramUsers(TelegramUserBaseModel, generics.ListAPIView):
    filter_backends = [DjangoFilterBackend,  OrderingFilter, SearchFilter]
    fields = [field.name for field in TelegramUser._meta.get_fields()]
    ordering_fields = ['user',]
    filterset_class = TelegramUserFilter



class GetAllLocations(LocationBaseModel, generics.ListAPIView):
    ...

class GetLocation(LocationBaseModel, generics.RetrieveAPIView):
    ...

class GetAllUserActions(UserActionBaseModel, generics.ListAPIView):
    filter_backends = [DjangoFilterBackend,  OrderingFilter, SearchFilter]
    fields = [field.name for field in UserAction._meta.get_fields()]
    ordering_fields = ['user',]
    filterset_class = UserActionsFilter

class GetConcreteUserActions(UserActionBaseModel, generics.ListAPIView):
    filter_backends = [DjangoFilterBackend,  OrderingFilter, SearchFilter]
    fields = [field.name for field in UserAction._meta.get_fields()]
    ordering_fields = ['user',]
    filterset_class = UserActionsFilter

    def get_queryset(self):
        external_id = self.kwargs['external_id']
        return UserAction.objects.filter(user__external_id=external_id)

class CreateUserAction(UserActionBaseModel, generics.CreateAPIView):
    serializer_class = SimpleUserActionSerializer
    

class GetActionType(ActionTypeBaseModel, generics.RetrieveAPIView):
    ...
