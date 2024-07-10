from app.database.dals.recording_dal import RecordingDAO


class RecordingService:
    @staticmethod
    async def get_one(recording_id):
        return await RecordingDAO.get_one(recording_id)

    @staticmethod
    async def get_all(self):
        return await RecordingDAO.get_all()

    @staticmethod
    async def create(data):
        if await RecordingService.get_one(data['id']):
            return False
        await RecordingDAO.create(data)
        return True

    @staticmethod
    async def update(data):
        recording_id = data.get("id")
        try:
            # TODO Сделать ограничение по времени, что бы запись не выходила за ограничения
            # TODO родительской недели
            recording = await RecordingService.get_one(recording_id)
            recording.date = data.get("date")
            recording.time = data.get("time")
            recording.slots_amount = data.get("slots_amount")
        except Exception:
            raise Exception('There is no such recording in db.')

        return await RecordingDAO.update(recording)

    @staticmethod
    async def delete(recording_id):
        await RecordingDAO.delete(recording_id)
