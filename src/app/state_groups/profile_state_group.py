from aiogram.fsm.state import StatesGroup, State


class ProfileStateGroup(StatesGroup):
    full_name = State()
