from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from Service.LocationService import LocationService
from Service.ActionTypeService import ActionTypeService


def get_locations_list():
    location_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    locations = LocationService.GetAllLocationsList()
    for location in locations:
        location_kb.row(
            KeyboardButton(location)
        )
    return location_kb


def choosing_action_with_location_kb(last_action_id):
    if last_action_id == 1:
        new_action_id = 2
    else:
        new_action_id = 1
    action_type = ActionTypeService.GetActionType(new_action_id)
    location_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    location_kb.row(
        KeyboardButton(action_type.get('name'))
    )
    return location_kb


def start_kb():
    start_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    start_kb.row(
        KeyboardButton('/start')
    )
    return start_kb


def request_location_kb():
    location_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    location_kb.row(
        KeyboardButton('Отправить геопозицию', request_location=True)
    )
    return location_kb


def get_result_kb():
    get_result_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    options = ['За сегодня', 'За вчера', 'За неделю', 'За месяц', 'За год']
    for option in options:
        get_result_kb.insert(KeyboardButton(option))
    get_result_kb.row(
        KeyboardButton('Мой промежуток')
    )
    return get_result_kb
