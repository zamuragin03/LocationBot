from Config import scheduler, dp, bot
from aiogram import Dispatcher
from random import randint
from Service import TelegramUserService

def CheckNotification():
    scheduler.add_job(check_notification, 'interval', minutes=10,
                      args=(dp,) )


async def check_notification(dp: Dispatcher):
    not_notificated_users = TelegramUserService.GetNotNotificatedTGUsers()
    for user in not_notificated_users:
        TelegramUserService.SetNotificationStatus(user.get('external_id'), status=True)
        try:
            await bot.send_message(
            user.get('external_id'),
            'Ваш профиль активирован, приятной работы'
        )
        except:
            ...