import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BOT_API
from app.routers.organization_router import organization_router
from app.routers.user_router import user_router
from app.routers.main_router import main_router

storage = MemoryStorage()
dp = Dispatcher()
dp.include_routers(
    main_router, user_router, organization_router
)


async def main() -> None:
    bot = Bot(BOT_API)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
