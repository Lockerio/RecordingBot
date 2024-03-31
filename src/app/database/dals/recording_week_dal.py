from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import RecordingWeek


class RecordingWeekDao:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, recording_week_id):
        async with self.session.begin():
            result = await self.session.execute(select(RecordingWeek).where(RecordingWeek.id == recording_week_id))
            return await result.scalar()

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(RecordingWeek))
            return result.scalars().all()

    async def create(self, data):
        recording_week = RecordingWeek(**data)
        async with self.session.begin():
            self.session.add(recording_week)
        return recording_week

    async def update(self, recording_week):
        async with self.session.begin():
            self.session.add(recording_week)
        return recording_week

    async def delete(self, recording_week_id):
        recording_week = await self.get_one(recording_week_id)
        async with self.session.begin():
            await self.session.delete(recording_week)
