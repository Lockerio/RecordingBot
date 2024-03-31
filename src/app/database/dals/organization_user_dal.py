from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User_Organization


class UserOrganizationDao:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, user_organization_id):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization).where(User_Organization.id == user_organization_id))
            return await result.scalar()

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(User_Organization))
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
