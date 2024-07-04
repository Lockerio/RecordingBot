from app.database.dals.organization_dal import OrganizationDAO


class OrganizationService:
    def __init__(self, serializer: OrganizationDAO):
        self.serializer = serializer

    async def get_one(self, organization_id):
        return await self.serializer.get_one(organization_id)

    async def get_one_by_invite_code(self, invite_code):
        return await self.serializer.get_one_by_invite_code(invite_code)

    async def get_all(self):
        return await self.serializer.get_all()

    async def get_all_by_user_id(self, user_id):
        return await self.serializer.get_all_by_user_id(user_id)

    async def create(self, data):
        return await self.serializer.create(data)

    async def update(self, data):
        organization_id = data.get("id")
        try:
            organization = await self.get_one(organization_id)
            organization.organization_name = data.get("organization_name")
            organization.invite_code = data.get("invite_code")
            organization.default_slots_amount = data.get("default_slots_amount")
        except Exception:
            raise Exception('There is no such user in db.')

        return await self.serializer.update(organization)

    async def delete(self, organization_id):
        await self.serializer.delete(organization_id)
