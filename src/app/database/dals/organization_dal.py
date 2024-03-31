from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Organization


class OrganizationDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, organization_id):
        async with self.session.begin():
            result = await self.session.execute(select(Organization).where(Organization.id == organization_id))
            return await result.scalar()

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(Organization))
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
