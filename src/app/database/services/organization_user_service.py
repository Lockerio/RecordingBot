from icecream import ic

from app.database.dals.organization_user_dal import UserOrganizationDAO


class UserOrganizationService:
    def __init__(self, serializer: UserOrganizationDAO):
        self.serializer = serializer

    async def get_one(self, user_organization_id):
        return await self.serializer.get_one(user_organization_id)

    async def get_one_active_by_user_id(self, user_id):
        return await self.serializer.get_one_active_by_user_id(user_id)

    async def get_one_by_user_id_and_organization_id(self, user_id, organization_id):
        return await self.serializer.get_one_by_user_id_and_organization_id(user_id, organization_id)

    async def get_all(self):
        return await self.serializer.get_all()

    async def get_all_by_user_id(self, user_id):
        return await self.serializer.get_all_by_user_id(user_id)

    async def create(self, data):
        await self.serializer.create(data)

    async def update(self, data):
        user_id = data.get("user_id")
        organization_id = data.get("organization_id")
        try:
            user_organization = await self.get_one_by_user_id_and_organization_id(user_id, organization_id)

            is_user_organization_current = data.get("is_current_organization")
            if is_user_organization_current:
                ic(is_user_organization_current)
                user_organization.is_current_organization = is_user_organization_current

        except Exception:
            raise Exception('There is no such user_organization in db.')

    async def delete(self, user_organization_id):
        await self.serializer.delete(user_organization_id)
