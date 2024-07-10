from app.database.dals.recording_week_dal import RecordingWeekDAO


class RecordingWeekService:
    @staticmethod
    async def get_one(recording_week_id):
        return await RecordingWeekDAO.get_one(recording_week_id)

    @staticmethod
    async def get_all():
        return await RecordingWeekDAO.get_all()

    @staticmethod
    async def create(data):
        if await RecordingWeekService.get_one(data['id']):
            return False
        await RecordingWeekDAO.create(data)
        return True
