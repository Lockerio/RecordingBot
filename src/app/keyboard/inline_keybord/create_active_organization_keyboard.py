from typing import Dict

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.callback_data.organization_callback_data import OrganizationCallbackData


async def create_active_organization_keyboard(organizations_dict: Dict, organization_id_to_be_inactive, buttons_per_row: int = 2):
    keyboard = InlineKeyboardBuilder()

    print(organizations_dict)

    for title, db_id in organizations_dict.items():
        callback_data = OrganizationCallbackData(
            organization_id_to_be_active=db_id,
            organization_id_to_be_inactive=organization_id_to_be_inactive
        ).pack()

        keyboard.button(
            text=title,
            callback_data=callback_data
        )

    keyboard.adjust(buttons_per_row)
    return keyboard.as_markup()


async def create_active_organization_keyboard_manual(organizations_dict: Dict, organization_id_to_be_inactive, buttons_per_row: int = 2):
    # Создаем список для хранения строк кнопок
    inline_keyboard = []

    # Временный список для хранения текущей строки кнопок
    row = []

    for title, db_id in organizations_dict.items():
        callback_data = f"organization-callback-data:{db_id}:{organization_id_to_be_inactive}"
        button = InlineKeyboardButton(text=title, callback_data=callback_data)
        row.append(button)

        # Если количество кнопок в строке достигло buttons_per_row, добавляем строку в клавиатуру и очищаем row
        if len(row) == buttons_per_row:
            inline_keyboard.append(row)
            row = []

    # Добавляем оставшиеся кнопки, если они есть
    if row:
        inline_keyboard.append(row)

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard