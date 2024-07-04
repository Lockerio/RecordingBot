from typing import Dict

from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_active_organization_keyboard(organizations_dict: Dict, buttons_per_row: int = 2):
    keyboard = InlineKeyboardBuilder()

    for title, db_id in organizations_dict.values():
        keyboard.button(text=title, callback_data=db_id)

    keyboard.adjust(buttons_per_row)
    return keyboard.as_markup()
