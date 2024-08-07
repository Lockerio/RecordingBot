import traceback

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from icecream import ic

from app.callback_data.organization_callback_data import OrganizationCallbackData
from app.database.services.organization_service import OrganizationService
from app.database.services.organization_user_service import UserOrganizationService
from app.database.services.user_service import UserService
from app.keyboard.inline_keybord.create_active_organization_keyboard import create_active_organization_keyboard, \
    create_active_organization_keyboard_manual
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
    user = await UserService.get_one_by_chat_id(message.chat.id)

    organization_data = {
        "user_id": user.id,
        "organization_name": organization_name,
        "default_slots_amount": int(default_slots_amount),
        "invite_code": invite_code
    }

    try:
        organization = await OrganizationService.create(organization_data)
        user_organization_data = {
            "user_id": user.id,
            "organization_id": organization.id,
            "is_current_organization": False
        }
        await UserOrganizationService.create(user_organization_data)

    except Exception as e:
        traceback.print_exc()
        await message.answer(await OrganizationMessagesTemplate.get_organization_creation_error_message())
    else:
        bot_info = await message.bot.me()

        await message.answer(await OrganizationMessagesTemplate.get_created_organization_message(organization_name))
        await message.answer(
            await OrganizationMessagesTemplate.get_organization_invite_code_message(
                organization_name,
                invite_code,
                bot_info.username
            ),
            parse_mode="MarkdownV2"
        )
    finally:
        await state.clear()


@organization_router.message(Command("set_organization"))
async def set_organization_handler(message: Message) -> None:
    try:
        user = await UserService.get_one_by_chat_id(message.chat.id)
        user_id = user.id

        active_user_organization = await UserOrganizationService.get_one_active_by_user_id(user_id)
        user_organizations = await UserOrganizationService.get_all_by_user_id(user_id)
        user_organizations_ids = [user_organization.organization_id for user_organization in user_organizations]
        active_user_organization_title = None
        active_user_organization_id = None

        if active_user_organization:
            active_organization = await OrganizationService.get_one(active_user_organization.organization_id)
            await user_organizations_ids.pop(active_organization.id)
            active_user_organization_title = active_organization.organization_name
            active_user_organization_id = active_organization.id

        organizations = [
            await OrganizationService.get_one(user_organization_id) for user_organization_id in user_organizations_ids
        ]

        organizations_data = {
            organization.organization_name: organization.id
            for organization in organizations
        }

        mark_up = await create_active_organization_keyboard(organizations_data, active_user_organization_id, 3)
        print(mark_up)
        repr(mark_up)
        await message.answer(
            await OrganizationMessagesTemplate.get_active_organization_message(active_user_organization_title),
            reply_markup=mark_up
        )
    except Exception:
        traceback.print_exc()


@organization_router.callback_query(OrganizationCallbackData.filter())
async def handle_organization_setting(callback_query: CallbackQuery, callback_data: OrganizationCallbackData) -> None:
    try:
        user = await UserService.get_one_by_chat_id(callback_query.message.chat.id)

        if callback_data.organization_id_to_be_inactive:
            user_organization_to_be_inactive = await UserOrganizationService.get_one(
                callback_data.organization_id_to_be_inactive)

            await UserOrganizationService.update({
                "user_id": user.id,
                "organization_id": user_organization_to_be_inactive.organization_id,
                "is_current_organization": False
            })

        user_organization_to_be_active = await UserOrganizationService.get_one_by_user_id_and_organization_id(
            user.id,
            callback_data.organization_id_to_be_active
        )

        await UserOrganizationService.update({
            "user_id": user.id,
            "organization_id": user_organization_to_be_active.organization_id,
            "is_current_organization": True
        })

        organization_to_be_active = await OrganizationService.get_one(user_organization_to_be_active.organization_id)

        await callback_query.answer(
            await OrganizationMessagesTemplate.get_success_organization_setting_message(
                organization_to_be_active.organization_name
            )
        )

    except Exception as e:
        traceback.print_exc()
        await callback_query.answer(await OrganizationMessagesTemplate.get_error_organization_setting_message())
