from .API import UserActionApi, TGUSerApi
import pandas as pd
from pathlib import Path
from datetime import datetime


class FileService:
    def GetResultByOption(option):
        options = {'За сегодня': 'today',
                   'За вчера': 'yesterday',
                   'За неделю': 'week',
                   'За месяц': 'month',
                   'За год': 'year'
                   }
        headers = ['Сотрудник',
                   'Объект вход',
                   'Объект выход',
                   'Открытие',
                   'Закрытие',
                   'Время работы'
                   ]

        df = pd.DataFrame(columns=headers)
        all_users = TGUSerApi.GetAllTelegramUsers()
        for user in all_users:
            actions = UserActionApi.GetConcreteUserLocations(
                external_id=user.get('external_id'), date=options.get(option))
            for action1, action2 in zip(actions[0::2], actions[1::2]):
                append_list = [
                    FileService.GetUser(user),
                    action1.get('location').get('name'),
                    action2.get('location').get('name'),
                    FileService.GetPrettyDateTime(action1.get('time')),
                    FileService.GetPrettyDateTime(action2.get('time')),
                    FileService.ConvertTwoDateTimesToStringInfo(action1.get('time'), action2.get('time'))]
                df.loc[len(df.index)] = append_list
        path_to_file = Path(__file__).parent.parent.joinpath("doc.xlsx")
        df.to_excel(path_to_file, index=False)
        return path_to_file

    def GetResultByCustomInterval(date_range_before, date_range_after):
        headers = ['Сотрудник',
                   'Объект вход',
                   'Объект выход',
                   'Открытие',
                   'Закрытие',
                   'Время работы'
                   ]

        df = pd.DataFrame(columns=headers)
        all_users = TGUSerApi.GetAllTelegramUsers()
        for user in all_users:
            actions = UserActionApi.GetConcreteUserLocations(
                external_id=user.get('external_id'), date_range_before=date_range_before, date_range_after=date_range_after)
            for action1, action2 in zip(actions[0::2], actions[1::2]):
                append_list = [
                    FileService.GetUser(user),
                    action1.get('location').get('name'),
                    action2.get('location').get('name'),
                    FileService.GetPrettyDateTime(action1.get('time')),
                    FileService.GetPrettyDateTime(action2.get('time')),
                    FileService.ConvertTwoDateTimesToStringInfo(action1.get('time'), action2.get('time'))]
                df.loc[len(df.index)] = append_list
        path_to_file = Path(__file__).parent.parent.joinpath("doc.xlsx")
        df.to_excel(path_to_file, index=False)
        return path_to_file

    def GetUser(user: dict):
        if user.get('username'):
            return user.get('username')
        return user.get('external_id')

    def ConvertSeconds(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)
        return f'{hours}ч, {minutes}м, {seconds}с'

    def ConvertTwoDateTimesToStringInfo(date_time1, date_time2):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        date1 = datetime.strptime(date_time1, format)
        date2 = datetime.strptime(date_time2, format)
        total_seconds1 = int(date1.timestamp())
        total_seconds2 = int(date2.timestamp())
        difference = abs(total_seconds2 - total_seconds1)
        return FileService.ConvertSeconds(difference)

    def GetPrettyDateTime(datetime_str):
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
        return datetime_obj.strftime("%d %B %Y года, %H:%M:%S")
