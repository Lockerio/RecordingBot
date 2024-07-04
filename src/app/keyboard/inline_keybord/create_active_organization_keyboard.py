from typing import Dict

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.callback_data.organization_callback_data import OrganizationCallbackData


async def create_active_organization_keyboard(organizations_dict: Dict, organization_id_to_be_inactive, buttons_per_row: int = 2):
    keyboard = InlineKeyboardBuilder()

    for title, db_id in organizations_dict.values():
        keyboard.button(
            text=title,
            callback_data=OrganizationCallbackData(
                organization_id_to_be_active=db_id,
                organization_id_to_be_inactive=organization_id_to_be_inactive
            ).pack()
        )

    keyboard.adjust(buttons_per_row)
    return keyboard.as_markup()
