from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.messages_templates.main_messages_template import MainMessagesTemplate


main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(await MainMessagesTemplate.get_start_message())
