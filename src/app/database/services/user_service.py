from app.database.dals.user_dal import UserDAO


class UserService:
    def __init__(self, serializer: UserDAO):
        self.serializer = serializer

    async def get_one(self, user_id):
        return await self.serializer.get_one(user_id)

    async def get_one_by_chat_id(self, chat_id):
        return await self.serializer.get_one_by_chat_id(chat_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True

    async def update(self, data):
        user_chat_id = data.get("chat_id")
        try:
            user = await self.get_one_by_chat_id(user_chat_id)
            user.user_fullname = data.get("user_fullname")
        except Exception:
            raise Exception('There is no such user in db.')

        return await self.serializer.update(user)

    async def delete(self, user_id):
        await self.serializer.delete(user_id)