from Config import dp, bot
from Service import QuestionService, TelegramUserService, UserActionService, GeoService, FileService
from Keyboards.keyboards import *
from States import FSMUser
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.utils.markdown import *


@dp.message_handler(commands=['result'], state='*')
async def result(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.chat.id,
        'Пожалуйста выберите промежуток для отчета:',
        reply_markup=get_result_kb()
    )
    await FSMUser.choosing_interval.set()


@dp.message_handler(state=FSMUser.choosing_interval)
async def choosing_interval(message: types.Message, state: FSMContext):
    if message.text == 'Мой промежуток':
        await bot.send_message(
            message.chat.id,
            'Отправьте начальную дату в формате ГГГГ-ММ-ДД',
            reply_markup=ReplyKeyboardRemove()
        )
        await FSMUser.typing_start_date.set()
        return
    path_to_file = FileService.GetResultByOption(message.text)
    await bot.send_document(
        message.chat.id,
        document=types.InputFile(str(path_to_file))
    )


@dp.message_handler(state=FSMUser.typing_start_date)
async def start_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_range_after'] = message.text
    await bot.send_message(
        message.chat.id,
        'Отправьте конечную дату в формате ГГГГ-ММ-ДД',
        reply_markup=ReplyKeyboardRemove()
    )
    await FSMUser.typing_end_date.set()


@dp.message_handler(state=FSMUser.typing_end_date)
async def end_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_range_before'] = message.text
    path_to_file = FileService.GetResultByOption(message.text)
    await bot.send_document(
        message.chat.id,
        document=types.InputFile(str(path_to_file))
    )



@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    TelegramUserService.CreateTelegramUser(message.from_user.id, message.from_user.username,
                                           message.from_user.first_name, message.from_user.last_name)
    await bot.send_message(
        message.chat.id,
        'какой-то текст тут нужен.'
    )
    if TelegramUserService.IsUserActive(message.from_user.id):
        last_action_id = ActionTypeService.GetLastUserActionId(
            message.from_user.id)
        message_to_send = 'Ваш профиль активирован'
        if last_action_id.get('id') == 1:
            last_location_name = LocationService.GetLocationNameById(
                last_action_id.get('id'))
            message_to_send += f'\nCейчас вы находитесь в {bold(f"{last_location_name}")}'
        await bot.send_message(
            message.chat.id,
            f'{message_to_send}\nВыберите филиал',
            reply_markup=get_locations_list(),
            parse_mode=types.ParseMode.MARKDOWN
        )
        await FSMUser.choosing_action.set()
    else:
        await bot.send_message(
            message.chat.id,
            'Ожидайте, пока ваш профиль будет подтверждён администрацией',
            reply_markup=ReplyKeyboardRemove()
        )


@dp.message_handler(state=FSMUser.choosing_action)
async def choosing_user_action(message: types.Message, state: FSMContext):
    selected_location_id = LocationService.GetLocationIdByName(message.text)
    last_action_id = ActionTypeService.GetLastUserActionId(
        message.from_user.id)
    await bot.send_message(
        message.chat.id,
        'Выберите действие',
        reply_markup=choosing_action_with_location_kb(last_action_id.get('id'))
    )
    async with state.proxy() as data:
        data['selected_id'] = selected_location_id

    await FSMUser.join_or_leave_action.set()


@dp.message_handler(filters.Text(equals='Вход'), state=FSMUser.join_or_leave_action)
async def join(message: types.Message):
    await bot.send_message(
        message.chat.id,
        'Пожалуйста отправьте вашу геолокацию',
        reply_markup=request_location_kb()
    )
    await FSMUser.sending_location.set()


@dp.message_handler(content_types=['location'], state=FSMUser.sending_location)
async def handle_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    async with state.proxy() as data:
        last_location_id = data['selected_id']
    result = GeoService.IsUserInArea(
        latitude=lat, longitude=lon, location_id=last_location_id)
    if result:
        user_id = TelegramUserService.GetTelegramUserId(message.from_user.id)
        try:
            # current_location_id = LocationService.GetLastLocationId(
            #     message.from_user.id)
            UserActionService.CreateUserAction(
                user=user_id, action=1, location=last_location_id)
        except:
            ...
        await bot.send_message(
            message.chat.id,
            'Отличная работа',
            reply_markup=start_kb()
        )
        await FSMUser.beginning.set()
    else:
        await bot.send_message(
            message.chat.id,
            'Вы должны быть в пределах выбранного филиала. Попробуйте снова',
            reply_markup=request_location_kb()
        )
        await FSMUser.sending_location.set()


@dp.message_handler(filters.Text(equals='Выход'), state=FSMUser.join_or_leave_action)
async def leave(message: types.Message, state: FSMContext):
    # LocationService.
    user_id = TelegramUserService.GetTelegramUserId(message.from_user.id)
    async with state.proxy() as data:
        UserActionService.CreateUserAction(
            user=user_id, action=2, location=data['selected_id'])
    await bot.send_message(
        message.chat.id,
        'Вы вышли из филиала',
        reply_markup=start_kb()
    )
    await FSMUser.beginning.set()
