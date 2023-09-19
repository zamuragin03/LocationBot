import requests
from Config import PROXY
import json
import json


class TGUSerApi:
    def CreateTelegramUser(external_id, username, first_name, second_name):
        requests.post(PROXY+'create_telegram_user', data=json.dumps({
            'external_id': external_id,
            'username': username,
            'first_name': first_name,
            'second_name': second_name,
        }), headers={
            "Content-type": "application/json",
        },)

    def GetTelegramUser(external_id) -> dict:
        return requests.get(PROXY+'get_telegram_user/' + str(external_id),).json()
    
    def GetAllTelegramUsers(**kwargs) -> dict:
        return requests.get(PROXY+'get_telegram_users',params=kwargs).json()

    def UpdateTelegramUser(external_id, **kwargs):
        return requests.patch(PROXY + 'update_telegram_user/' + str(external_id), data=kwargs)

class LocationApi:

    def GetLocation(id)->dict:
        return requests.get(f'{PROXY}get_location/{id}').json()

    def GetAllLocations():
        return requests.get(f'{PROXY}get_locations').json()


class ActionTypeApi:
    def GetActionType(id) -> dict:
        return requests.get(f'{PROXY}get_action_type/{id}').json()

   


class UserActionApi:
    def CreateUserAction(user, action, location):
        return requests.post(f'{PROXY}create_user_action', data=json.dumps({
            'user': user,
            'action': action,
            'location': location
        }), headers={
            "Content-type": "application/json",
        },)

    def GetUserActions(**kwargs):
        return requests.get(f'{PROXY}get_user_actions', params=kwargs).json()
    
    def GetConcreteUserLocations(external_id,**kwargs):
        return requests.get(f'{PROXY}get_concrete_user_actions/{external_id}', params=kwargs).json()

