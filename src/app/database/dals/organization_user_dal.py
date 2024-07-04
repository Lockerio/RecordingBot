from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User_Organization


class UserOrganizationDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, user_organization_id):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization).where(User_Organization.id == user_organization_id))
            return await result.scalar()

    async def get_one_active_by_user_id(self, user_id):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization).where((User_Organization.id == user_id) & (User_Organization.is_current_organization == True)))
            organization = result.scalar_one_or_none()
            return organization

    async def get_one_by_user_id_and_organization_id(self, user_id, organization_id):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization).where((User_Organization.id == user_id) & (User_Organization.organization_id == organization_id)))
            organization = result.scalar_one_or_none()
            return organization

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization))
            return result.scalars().all()

    async def get_all_by_user_id(self, user_id):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization).where(User_Organization.user_id == user_id))
            return result.scalars().all()

    async def create(self, data):
        user_organization = User_Organization(**data)
        async with self.session.begin():
            self.session.add(user_organization)
        return user_organization

    async def update(self, user_organization):
        async with self.session.begin():
            self.session.add(user_organization)
        return user_organization

    async def delete(self, user_organization_id):
        user_organization = await self.get_one(user_organization_id)
        async with self.session.begin():
            await self.session.delete(user_organization)
