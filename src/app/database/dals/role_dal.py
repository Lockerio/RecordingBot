from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import session_maker
from app.database.models import Role


class RoleDAO:
    @staticmethod
    async def get_one(role_id):
        async with session_maker() as session:
            result = await session.execute(select(Role).where(Role.id == role_id))
            role = result.scalar_one_or_none()
            return role

    @staticmethod
    async def get_one_by_title(title):
        async with session_maker() as session:
            result = await session.execute(select(Role).where(Role.title == title))
            role = result.scalar_one_or_none()
            return role

    @staticmethod
    async def get_all():
        async with session_maker() as session:
            result = await session.execute(select(Role))
            return result.scalars().all()

    @staticmethod
    async def create(data):
        role = Role(**data)
        async with session_maker() as session:
            session.add(role)
            await session.commit()
        return role
