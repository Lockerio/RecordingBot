from app.database.dals.organization_dal import OrganizationDAO


class OrganizationService:
    @staticmethod
    async def get_one(organization_id):
        return await OrganizationDAO.get_one(organization_id)

    @staticmethod
    async def get_one_by_invite_code(invite_code):
        return await OrganizationDAO.get_one_by_invite_code(invite_code)

    @staticmethod
    async def get_all():
        return await OrganizationDAO.get_all()

    @staticmethod
    async def get_all_by_user_id(user_id):
        return await OrganizationDAO.get_all_by_user_id(user_id)

    @staticmethod
    async def create(data):
        return await OrganizationDAO.create(data)

    @staticmethod
    async def update(data):
        organization_id = data.get("id")
        try:
            organization = await OrganizationService.get_one(organization_id)
            organization.organization_name = data.get("organization_name")
            organization.invite_code = data.get("invite_code")
            organization.default_slots_amount = data.get("default_slots_amount")
        except Exception:
            raise Exception('There is no such user in db.')

        return await OrganizationDAO.update(organization)

    @staticmethod
    async def delete(organization_id):
        await OrganizationDAO.delete(organization_id)
