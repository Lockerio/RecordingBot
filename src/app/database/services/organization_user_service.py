from app.database.dals.organization_user_dal import UserOrganizationDAO


class UserOrganizationService:
    @staticmethod
    async def get_one(user_organization_id):
        return await UserOrganizationDAO.get_one(user_organization_id)

    @staticmethod
    async def get_one_active_by_user_id(user_id):
        return await UserOrganizationDAO.get_one_active_by_user_id(user_id)

    @staticmethod
    async def get_one_by_user_id_and_organization_id(user_id, organization_id):
        return await UserOrganizationDAO.get_one_by_user_id_and_organization_id(user_id, organization_id)

    @staticmethod
    async def get_all(self):
        return await UserOrganizationDAO.get_all()

    @staticmethod
    async def get_all_by_user_id(user_id):
        return await UserOrganizationDAO.get_all_by_user_id(user_id)

    @staticmethod
    async def create(data):
        await UserOrganizationDAO.create(data)

    @staticmethod
    async def update(data):
        user_id = data.get("user_id")
        organization_id = data.get("organization_id")
        try:
            user_organization = await UserOrganizationService.get_one_by_user_id_and_organization_id(user_id, organization_id)

            is_user_organization_current = data.get("is_current_organization")
            if is_user_organization_current:
                user_organization.is_current_organization = is_user_organization_current

        except Exception:
            raise Exception('There is no such user_organization in db.')

    @staticmethod
    async def delete(user_organization_id):
        await UserOrganizationDAO.delete(user_organization_id)
