from .API import TGUSerApi


class TelegramUserService():
    def IsUserActive(external_id):
        return TGUSerApi.GetTelegramUser(external_id=external_id).get('is_active')
    def GetTelegramUserId(external_id):
        return TGUSerApi.GetTelegramUser(external_id=external_id).get('id')
    def CreateTelegramUser(external_id, username, first_name, second_name):
        return TGUSerApi.CreateTelegramUser(external_id, username, first_name, second_name)
    def GetNotNotificatedTGUsers():
        return TGUSerApi.GetAllTelegramUsers(is_notificated=False,is_active=True)
    def SetNotificationStatus(external_id,status):
        return TGUSerApi.UpdateTelegramUser(external_id, is_notificated=status)
