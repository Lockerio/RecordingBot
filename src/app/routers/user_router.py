from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.services.user_service import UserService
from app.messages_templates.user_messages_template import UserMessagesTemplate
from app.state_groups.profile_state_group import ProfileStateGroup


user_router = Router()


@user_router.message(Command("create"))
async def command_create_handler(message: Message, state: FSMContext) -> None:
    await message.answer(await UserMessagesTemplate.get_create_profile_message())
    await state.set_state(ProfileStateGroup.full_name)


@user_router.message(ProfileStateGroup.full_name)
async def create_profile_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(user_fullname=message.text)
    data = await state.get_data()
    user_fullname = data["user_fullname"]
    user_data = {
        "chat_id": message.chat.id,
        "user_fullname": user_fullname
    }

    try:
        await UserService.create(user_data)
    except:
        await message.answer(await UserMessagesTemplate.get_profile_creation_error_message())
    else:
        await message.answer(await UserMessagesTemplate.get_profile_creation_success_message())
    finally:
        await state.clear()
