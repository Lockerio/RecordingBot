from app.database.dals.role_dal import RoleDAO


class RoleService:
    @staticmethod
    async def get_one(role_id):
        return await RoleDAO.get_one(role_id)

    @staticmethod
    async def get_one_by_title(title):
        return await RoleDAO.get_one_by_title(title)

    @staticmethod
    async def get_all():
        return await RoleDAO.get_all()

    @staticmethod
    async def create(data):
        await RoleDAO.create(data)
