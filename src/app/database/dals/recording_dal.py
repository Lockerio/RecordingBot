from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import session_maker
from app.database.models import Recording


class RecordingDAO:
    @staticmethod
    async def get_one(recording_id):
        async with session_maker() as session:
            result = await session.execute(select(Recording).where(Recording.id == recording_id))
            return await result.scalar()

    @staticmethod
    async def get_all():
        async with session_maker() as session:
            result = await session.execute(select(Recording))
            return result.scalars().all()

    @staticmethod
    async def create(data):
        recording = Recording(**data)
        async with session_maker() as session:
            session.add(recording)
            await session.commit()
        return recording

    @staticmethod
    async def update(recording):
        async with session_maker() as session:
            session.add(recording)
            await session.commit()
        return recording

    @staticmethod
    async def delete(recording_id):
        recording = await RecordingDAO.get_one(recording_id)
        async with session_maker() as session:
            await session.delete(recording)
            await session.commit()
