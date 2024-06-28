from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Role


class RoleDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, role_id):
        async with self.session.begin():
            result = await self.session.execute(select(Role).where(Role.id == role_id))
            role = result.scalar_one_or_none()
            return role

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(Role))
            return result.scalars().all()

    async def create(self, data):
        role = Role(**data)
        async with self.session.begin():
            self.session.add(role)
        return role
