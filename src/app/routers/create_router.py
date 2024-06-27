from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.container import user_service
from app.messages_templates.message_templates import CREATE_PROFILE_MESSAGE, PROFILE_CREATION_ERROR_MESSAGE, \
    PROFILE_CREATED_MESSAGE
from app.state_groups.profile_state_group import ProfileStateGroup


create_router = Router()


@create_router.message(Command("create"))
async def command_create_handler(message: Message, state: FSMContext) -> None:
    await message.answer(CREATE_PROFILE_MESSAGE)
    await state.set_state(ProfileStateGroup.full_name)


@create_router.message(ProfileStateGroup.full_name)
async def create_profile_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(user_fullname=message.text)
    data = await state.get_data()
    user_fullname = data["user_fullname"]
    user_data = {
        "chat_id": message.chat.id,
        "user_fullname": user_fullname
    }

    try:
        await user_service.create(user_data)
    except:
        await message.answer(PROFILE_CREATION_ERROR_MESSAGE)
    else:
        await message.answer(PROFILE_CREATED_MESSAGE)
    finally:
        await state.clear()
