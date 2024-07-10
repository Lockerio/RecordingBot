from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.constants.roles import OWNER
from app.database.services.role_service import RoleService
from app.database.services.user_service import UserService
from app.messages_templates.role_messages_template import RoleMessagesTemplate
from app.state_groups.role_state_group import RoleStateGroup
from app.utils.hash_string import hash_string

role_router = Router()


@role_router.message(Command("set_owner_role"))
async def set_owner_role_command_handler(message: Message, state: FSMContext):
    role = await RoleService.get_one_by_title(OWNER)

    if role.password_hash:
        await state.update_data(password_hash=message.text)
        await state.update_data(role_id=role.id)
        await state.set_state(RoleStateGroup.password)

    else:
        await UserService.update({
            "chat_id": message.chat.id,
            "role_id": role.id
        })
        await message.answer(await RoleMessagesTemplate.get_role_setting_success_message())


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
            await UserService.create(user_data)
        except:
            await message.answer(await RoleMessagesTemplate.get_role_setting_error_message())
        else:
            await message.answer(await RoleMessagesTemplate.get_role_setting_success_message())
        finally:
            await state.clear()
    else:
        await message.answer(await RoleMessagesTemplate.get_incorrect_password_message())
        await state.clear()
