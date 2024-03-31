from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Recording


class RecordingDao:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, recording_id):
        async with self.session.begin():
            result = await self.session.execute(select(Recording).where(Recording.id == recording_id))
            return await result.scalar()

    async def get_all(self):
        async with self.session.begin():
            result = await self.session.execute(select(Recording))
            return result.scalars().all()

    async def create(self, data):
        recording = Recording(**data)
        async with self.session.begin():
            self.session.add(recording)
        return recording

    async def update(self, recording):
        async with self.session.begin():
            self.session.add(recording)
        return recording

    async def delete(self, recording_id):
        recording = await self.get_one(recording_id)
        async with self.session.begin():
            await self.session.delete(recording)
