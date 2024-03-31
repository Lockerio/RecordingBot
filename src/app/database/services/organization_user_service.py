from app.database.dals.organization_user_dal import UserOrganizationDAO


class UserOrganizationService:
    def __init__(self, serializer: UserOrganizationDAO):
        self.serializer = serializer

    async def get_one(self, user_organization_id):
        return await self.serializer.get_one(user_organization_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def get_all_user_id(self, user_id):
        return await self.serializer.get_all_user_id(user_id)

    async def create(self, data):
        if await self.get_one(data['id']):
            return False
        await self.serializer.create(data)
        return True

    async def delete(self, user_organization_id):
        await self.serializer.delete(user_organization_id)