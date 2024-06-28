from app.database.dals.role_dal import RoleDAO


class RoleService:
    def __init__(self, serializer: RoleDAO):
        self.serializer = serializer

    async def get_one(self, role_id):
        return await self.serializer.get_one(role_id)

    async def get_one_by_title(self, title):
        return await self.serializer.get_one_by_title(title)

    async def get_all(self):
        return await self.serializer.get_all()

    async def create(self, data):
        await self.serializer.create(data)
