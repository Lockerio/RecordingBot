from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.container import user_service
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
    invite_code = hash_string(organization_name)
    user_data = {
        "user_id": message.chat.id,
        "organization_name": organization_name,
        "default_slots_amount": default_slots_amount,
        "invite_code": invite_code
    }

    try:
        await user_service.create(user_data)
    except:
        await message.answer(CREATED_ORGANIZATION_MESSAGE)
        await message.answer(GET_ORGANIZATION_INVITE_CODE_MESSAGE + invite_code)
    else:
        await message.answer(ORGANIZATION_CREATION_ERROR_MESSAGE)
    finally:
        await state.clear()
