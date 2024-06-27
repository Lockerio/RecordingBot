import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from app.config import BOT_API
from app.messages_templates.message_templates import START_MESSAGE
from app.routers.create_router import create_router
from app.routers.main_router import main_router

storage = MemoryStorage()
dp = Dispatcher()
dp.include_routers(
    main_router, create_router
)


async def main() -> None:
    bot = Bot(BOT_API)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
