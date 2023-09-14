from .API import UserActionApi


class UserActionService:

    def CreateUserAction(user, action, location):
        return UserActionApi.CreateUserAction(user, action, location)
