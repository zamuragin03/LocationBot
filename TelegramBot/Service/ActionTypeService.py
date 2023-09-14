from .API import ActionTypeApi, UserActionApi


class ActionTypeService:
    def GetActionType(id):
        return ActionTypeApi.GetActionType(id)

    def GetLastUserActionId(external_id):
        try:
            return UserActionApi.GetConcreteUserLocations(external_id=external_id)[-1].get('action')
        except:
            return None
    
    def GetLastUserAction(external_id)->dict:
        try:
            return UserActionApi.GetConcreteUserLocations(external_id=external_id)[-1]
        except:
            return None
