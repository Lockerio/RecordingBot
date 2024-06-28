from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.constants.roles import OWNER
from app.database.container import role_service, user_service
from app.messages_templates.role_messages_template import INCORRECT_PASSWORD_MESSAGE, SET_ROLE_ERROR_MESSAGE, \
    SET_ROLE_SUCCESS_MESSAGE
from app.state_groups.role_state_group import RoleStateGroup
from app.utils.hash_string import hash_string

role_router = Router()


@role_router.message(Command("set_owner_role"))
async def set_owner_role_command_handler(message: Message, state: FSMContext):
    role = await role_service.get_one_by_title(OWNER)

    if role.password_hash:
        await state.update_data(password_hash=message.text)
        await state.update_data(role_id=role.id)
        await state.set_state(RoleStateGroup.password)

    else:
        user_service.update({
            "chat_id": message.chat.id,
            "role_id": role.id
        })


@role_router.message(RoleStateGroup.password)
async def set_owner_role_handler(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    password_hash_from_state = data["password_hash"]
    password = data["password"]
    password_hash = await hash_string(password)

    if password_hash_from_state == password_hash:
        user_data = {
            "chat_id": message.chat.id,
            "role_id": data["role_id"]
        }

        try:
            await user_service.create(user_data)
        except:
            await message.answer(SET_ROLE_ERROR_MESSAGE)
        else:
            await message.answer(SET_ROLE_SUCCESS_MESSAGE)
        finally:
            await state.clear()
    else:
        await message.answer(INCORRECT_PASSWORD_MESSAGE)
        await state.clear()
