import traceback

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.container import organization_service, user_service
from app.messages_templates.organization_messages_template import OrganizationMessagesTemplate
from app.state_groups.organization_state_group import OrganizationStateGroup
from app.utils.hash_string import hash_string

organization_router = Router()


@organization_router.message(Command("create_organization"))
async def command_create_organization_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(OrganizationStateGroup.organization_name)
    await message.answer(await OrganizationMessagesTemplate.get_create_organization_message())


@organization_router.message(OrganizationStateGroup.organization_name)
async def wait_organization_title_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(organization_name=message.text)
    await message.answer(await OrganizationMessagesTemplate.get_create_organization_slots_message())
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
        await message.answer(await OrganizationMessagesTemplate.get_organization_creation_error_message())
    else:
        await message.answer(await OrganizationMessagesTemplate.get_created_organization_message(organization_name))
        await message.answer(await OrganizationMessagesTemplate.get_organization_invite_code_message(organization_name, invite_code), parse_mode="MarkdownV2")
    finally:
        await state.clear()


@organization_router.message(Command("set_organization"))
async def set_organization_handler(message: Message) -> None:
    pass
