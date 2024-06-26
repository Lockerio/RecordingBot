from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User


class UserDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, user_id):
        async with self.session.begin():
            result = await self.session.execute(select(User).where(User.id == user_id))
            return await result.scalar()

    async def get_one_by_chat_id(self, chat_id):
        async with self.session.begin():
            result = await self.session.execute(select(User).where(User.chat_id == chat_id))
            user = result.scalar_one_or_none()
            return user

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(User))
            return result.scalars().all()

    async def create(self, data):
        user = User(**data)
        async with self.session.begin():
            self.session.add(user)
        return user

    async def update(self, user):
        async with self.session.begin():
            self.session.add(user)
        return user

    async def delete(self, user_id):
        user = await self.get_one(user_id)
        async with self.session.begin():
            await self.session.delete(user)
