import asyncio

from app.constants.roles import ADMIN, OWNER, USER
from app.database.container import role_service


async def set_up_roles():
    roles = [ADMIN, OWNER, USER]

    for role in roles:
        await role_service.create({"title": role})


if __name__ == "__main__":
    asyncio.run(set_up_roles())
