from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMUser(StatesGroup):
    beginning = State()
    choosing_action = State()
    join_or_leave_action = State()
    sending_location = State()

    choosing_interval = State()
    typing_start_date = State()
    typing_end_date = State()