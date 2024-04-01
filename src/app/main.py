import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Message

from app.config import BOT_API

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_data = {
        "chat_id": message.chat.id,
        "user_fullname": message.from_user.full_name
    }


    await message.answer(f"Hello, {message.from_user.full_name}!")


async def main() -> None:
    bot = Bot(BOT_API, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
