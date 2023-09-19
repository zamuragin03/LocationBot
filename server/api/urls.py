from django.urls import *
from api.views import *

urlpatterns = [
    path('create_telegram_user', CreateTelegramUser.as_view()),
    path('get_telegram_user/<int:external_id>', GetTelegramUser.as_view()),
    path('update_telegram_user/<int:external_id>', UpdateTelegramUser.as_view()),
    path('get_telegram_users', GetTelegramUsers.as_view()),
    path('get_locations', GetAllLocations.as_view()),
    path('get_location/<int:pk>', GetLocation.as_view()),
    path('get_user_actions', GetAllUserActions.as_view()),
    path('create_user_action', CreateUserAction.as_view()),
    path('get_concrete_user_actions/<int:external_id>', GetConcreteUserActions.as_view()),
    path('get_action_type/<int:pk>', GetActionType.as_view()),
]