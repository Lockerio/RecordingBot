from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Organization


class OrganizationDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, organization_id):
        async with self.session.begin():
            result = await self.session.execute(select(Organization).where(Organization.id == organization_id))
            organization = result.scalar_one_or_none()
            return organization

    async def get_one_by_invite_code(self, invite_code):
        async with self.session.begin():
            result = await self.session.execute(select(Organization).where(Organization.invite_code == invite_code))
            organization = result.scalar_one_or_none()
            return organization

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(Organization))
            return result.scalars().all()

    async def get_all_by_user_id(self, user_id):
        async with self.session.begin():
            result = await self.session.execute(select(Organization).where(Organization.user_id == user_id))
            return result.scalars().all()

    async def create(self, data):
        organization = Organization(**data)
        async with self.session.begin():
            self.session.add(organization)
        return organization

    async def update(self, organization):
        async with self.session.begin():
            self.session.add(organization)
        return organization

    async def delete(self, organization_id):
        organization = await self.get_one(organization_id)
        async with self.session.begin():
            await self.session.delete(organization)
