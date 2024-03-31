from app.database.dals.recording_week_dal import RecordingWeekDAO


class RecordingWeekService:
    def __init__(self, serializer: RecordingWeekDAO):
        self.serializer = serializer

    async def get_one(self, recording_week_id):
        return await self.serializer.get_one(recording_week_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True
