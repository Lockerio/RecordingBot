from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.messages_templates.message_templates import START_MESSAGE


main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(START_MESSAGE)
