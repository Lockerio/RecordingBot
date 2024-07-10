from app.database.dals.user_dal import UserDAO


class UserService:
    @staticmethod
    async def get_one(user_id):
        return await UserDAO.get_one(user_id)

    @staticmethod
    async def get_one_by_chat_id(chat_id):
        return await UserDAO.get_one_by_chat_id(chat_id)

    @staticmethod
    async def get_all():
        return await UserDAO.get_all()

    @staticmethod
    async def create(data):
        if await UserService.get_one_by_chat_id(data['chat_id']):
            return False
        await UserDAO.create(data)
        return True

    @staticmethod
    async def update(data):
        user_chat_id = data.get("chat_id")
        try:
            user = await UserService.get_one_by_chat_id(user_chat_id)

            user_fullname = data.get("user_fullname")
            if user_fullname:
                user.user_fullname = user_fullname

            role_id = data.get("role_id")
            if role_id:
                user.role_id = role_id

        except Exception:
            raise Exception('There is no such user in db.')

        return await UserDAO.update(user)

    @staticmethod
    async def delete(user_id):
        await UserDAO.delete(user_id)
