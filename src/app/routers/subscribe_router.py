import traceback

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.container import user_service, user_organization_service, organization_service
from app.messages_templates.subscribe_message_template import WAIT_INVITE_CODE_MESSAGE, SUBSCRIPTION_ERROR_MESSAGE, \
    SUBSCRIPTION_SUCCESS_MESSAGE
from app.state_groups.subscribe_state_group import SubscribeStateGroup

subscribe_router = Router()


@subscribe_router.message(Command("subscribe_to_organization"))
async def subscribe_to_organization_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(SubscribeStateGroup.invite_code)
    await message.answer(WAIT_INVITE_CODE_MESSAGE)


@subscribe_router.message(SubscribeStateGroup.invite_code)
async def subscribed_to_organization_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(invite_code=message.text)
    data = await state.get_data()
    invite_code = data["invite_code"]
    user = await user_service.get_one_by_chat_id(message.chat.id)
    organization = await organization_service.get_one_by_invite_code(invite_code)

    user_organization_data = {
        "user_id": user.id,
        "organization_id": organization.id
    }

    try:
        await user_organization_service.create(user_organization_data)
    except Exception as e:
        traceback.print_exc()
        await message.answer(SUBSCRIPTION_ERROR_MESSAGE)
    else:
        await message.answer(f"{SUBSCRIPTION_SUCCESS_MESSAGE} **{organization.organization_name}**", parse_mode="MarkdownV2")
    finally:
        await state.clear()