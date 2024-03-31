from app.database.dals.recording_dal import RecordingDAO


class RecordingService:
    def __init__(self, serializer: RecordingDAO):
        self.serializer = serializer

    async def get_one(self, recording_id):
        return await self.serializer.get_one(recording_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True

    async def update(self, data):
        recording_id = data.get("id")
        try:
            # TODO Сделать ограничение по времени, что бы запись не выходила за ограничения
            # TODO родительской недели
            recording = await self.get_one(recording_id)
            recording.date = data.get("date")
            recording.time = data.get("time")
            recording.slots_amount = data.get("slots_amount")
        except Exception:
            raise Exception('There is no such recording in db.')

        return await self.serializer.update(recording)

    async def delete(self, recording_id):
        await self.serializer.delete(recording_id)