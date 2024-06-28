from aiogram.fsm.state import StatesGroup, State


class SubscribeStateGroup(StatesGroup):
    invite_code = State()
