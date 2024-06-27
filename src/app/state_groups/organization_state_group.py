from aiogram.fsm.state import StatesGroup, State


class OrganizationStateGroup(StatesGroup):
    organization_name = State()
    default_slots_amount = State()
