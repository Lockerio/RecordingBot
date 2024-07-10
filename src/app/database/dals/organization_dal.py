from sqlalchemy import select

from app.database.database import session_maker
from app.database.models import Organization


class OrganizationDAO:
    @staticmethod
    async def get_one(organization_id):
        async with session_maker() as session:
            result = await session.execute(select(Organization).where(Organization.id == organization_id))
            organization = result.scalar_one_or_none()
            return organization

    @staticmethod
    async def get_one_by_invite_code(invite_code):
        async with session_maker() as session:
            result = await session.execute(select(Organization).where(Organization.invite_code == invite_code))
            organization = result.scalar_one_or_none()
            return organization

    @staticmethod
    async def get_all():
        async with session_maker() as session:
            result = await session.execute(select(Organization))
            return result.scalars().all()

    @staticmethod
    async def get_all_by_user_id(user_id):
        async with session_maker() as session:
            result = await session.execute(select(Organization).where(Organization.user_id == user_id))
            return result.scalars().all()

    @staticmethod
    async def create(data):
        organization = Organization(**data)
        async with session_maker() as session:
            session.add(organization)
            await session.commit()
        return organization

    @staticmethod
    async def update(organization):
        async with session_maker() as session:
            session.add(organization)
            await session.commit()
        return organization

    @staticmethod
    async def delete(organization_id):
        organization = await OrganizationDAO.get_one(organization_id)
        async with session_maker() as session:
            await session.delete(organization)
            await session.commit()
