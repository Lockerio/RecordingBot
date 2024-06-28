import traceback

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.container import organization_service, user_service
from app.messages_templates.organization_messages_template import CREATE_ORGANIZATION_MESSAGE, \
    CREATE_ORGANIZATION_SLOTS_MESSAGE, ORGANIZATION_CREATION_ERROR_MESSAGE, CREATED_ORGANIZATION_MESSAGE, \
    GET_ORGANIZATION_INVITE_CODE_MESSAGE
from app.state_groups.organization_state_group import OrganizationStateGroup
from app.utils.hash_string import hash_string

organization_router = Router()


@organization_router.message(Command("create_organization"))
async def command_create_organization_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(OrganizationStateGroup.organization_name)
    await message.answer(CREATE_ORGANIZATION_MESSAGE)


@organization_router.message(OrganizationStateGroup.organization_name)
async def wait_organization_title_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(organization_name=message.text)
    await message.answer(CREATE_ORGANIZATION_SLOTS_MESSAGE)
    await state.set_state(OrganizationStateGroup.default_slots_amount)


@organization_router.message(OrganizationStateGroup.default_slots_amount)
async def wait_organization_title_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(default_slots_amount=message.text)
    data = await state.get_data()

    organization_name = data["organization_name"]
    default_slots_amount = data["default_slots_amount"]
    invite_code = await hash_string(organization_name)
    user = await user_service.get_one_by_chat_id(message.chat.id)

    organization_data = {
        "user_id": user.id,
        "organization_name": organization_name,
        "default_slots_amount": int(default_slots_amount),
        "invite_code": invite_code
    }

    try:
        await organization_service.create(organization_data)
    except Exception as e:
        traceback.print_exc()
        await message.answer(ORGANIZATION_CREATION_ERROR_MESSAGE)
    else:
        await message.answer(CREATED_ORGANIZATION_MESSAGE)
        await message.answer(f"{GET_ORGANIZATION_INVITE_CODE_MESSAGE} `{invite_code}`", parse_mode="MarkdownV2")
    finally:
        await state.clear()


@organization_router.message(Command("set_organization"))
async def set_organization_handler(message: Message) -> None:
    pass