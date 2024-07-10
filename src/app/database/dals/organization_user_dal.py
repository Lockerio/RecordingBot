from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import session_maker
from app.database.models import User_Organization


class UserOrganizationDAO:
    @staticmethod
    async def get_one(user_organization_id):
        async with session_maker() as session:
            result = await session.execute(select(User_Organization).where(User_Organization.id == user_organization_id))
            organization = result.scalar_one_or_none()
            return organization

    @staticmethod
    async def get_one_active_by_user_id(user_id):
        async with session_maker() as session:
            result = await session.execute(select(User_Organization).where((User_Organization.id == user_id) & (User_Organization.is_current_organization == True)))
            organization = result.scalar_one_or_none()
            return organization

    @staticmethod
    async def get_one_by_user_id_and_organization_id(user_id, organization_id):
        async with session_maker() as session:
            result = await session.execute(select(User_Organization).where((User_Organization.user_id == user_id) & (User_Organization.organization_id == organization_id)))
            organization = result.scalar_one_or_none()
            return organization

    @staticmethod
    async def get_all():
        async with session_maker() as session:
            result = await session.execute(select(User_Organization))
            return result.scalars().all()

    @staticmethod
    async def get_all_by_user_id(user_id):
        async with session_maker() as session:
            result = await session.execute(select(User_Organization).where(User_Organization.user_id == user_id))
            return result.scalars().all()

    @staticmethod
    async def create(data):
        user_organization = User_Organization(**data)
        async with session_maker() as session:
            session.add(user_organization)
            await session.commit()
        return user_organization

    @staticmethod
    async def update(user_organization):
        async with session_maker() as session:
            session.add(user_organization)
            await session.commit()
        return user_organization

    @staticmethod
    async def delete(user_organization_id):
        user_organization = await UserOrganizationDAO.get_one(user_organization_id)
        async with session_maker() as session:
            await session.delete(user_organization)
            await session.commit()
