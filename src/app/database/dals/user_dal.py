from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import session_maker
from app.database.models import User


class UserDAO:
    @staticmethod
    async def get_one(user_id):
        async with session_maker() as session:
            result = await session.execute(select(User).where(User.id == user_id))
            return await result.scalar()

    @staticmethod
    async def get_one_by_chat_id(chat_id):
        async with session_maker() as session:
            result = await session.execute(select(User).where(User.chat_id == chat_id))
            user = result.scalar_one_or_none()
            return user

    @staticmethod
    async def get_all():
        async with session_maker() as session:
            result = await session.execute(select(User))
            return result.scalars().all()

    @staticmethod
    async def create(data):
        user = User(**data)
        async with session_maker() as session:
            session.add(user)
            await session.commit()
        return user

    @staticmethod
    async def update(user):
        async with session_maker() as session:
            session.add(user)
            await session.commit()
        return user

    @staticmethod
    async def delete(user_id):
        user = await UserDAO.get_one(user_id)
        async with session_maker() as session:
            await session.delete(user)
            await session.commit()
