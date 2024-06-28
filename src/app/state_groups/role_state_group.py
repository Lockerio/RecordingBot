from aiogram.fsm.state import StatesGroup, State


class RoleStateGroup(StatesGroup):
    password = State()
