from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import session_maker
from app.database.models import RecordingWeek


class RecordingWeekDAO:
    @staticmethod
    async def get_one(recording_week_id):
        async with session_maker() as session:
            result = await session.execute(select(RecordingWeek).where(RecordingWeek.id == recording_week_id))
            return await result.scalar()

    @staticmethod
    async def get_all():
        async with session_maker() as session:
            result = await session.execute(select(RecordingWeek))
            return result.scalars().all()

    @staticmethod
    async def create(data):
        recording_week = RecordingWeek(**data)
        async with session_maker() as session:
            session.add(recording_week)
            await session.commit()
        return recording_week

    @staticmethod
    async def update(recording_week):
        async with session_maker() as session:
            session.add(recording_week)
            await session.commit()
        return recording_week

    @staticmethod
    async def delete(recording_week_id):
        recording_week = await RecordingWeekDAO.get_one(recording_week_id)
        async with session_maker() as session:
            await session.delete(recording_week)
            await session.commit()
