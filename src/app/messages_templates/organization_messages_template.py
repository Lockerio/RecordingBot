from app.constants.bot_info import BOT_LINK


class OrganizationMessageTemplate:
    @staticmethod
    async def get_create_organization_message(self):
        message = "Давайте создадим вашу 'организацию'. Для этого введите ее наименование"
        return message

    @staticmethod
    async def get_create_organization_slots_message():
        message = "Теперь, необходимо ввести количество мест на занятие (введите число)"
        return message

    @staticmethod
    async def get_created_organization_message(organization_title):
        message = (f"Ваша организация '{organization_title}' успешно создана! "
                   "В следующем сообщении будет инвайт код, с помощью которого человек сможет подписаться "
                   "на уведомления вашей организации.) "
                   "Просто перешлите ему следующее сообщение-приглашение.")
        return message

    @staticmethod
    async def get_organization_invite_code_message(organization_title, invite_code):
        message = (f"Для подписки на {organization_title} нужно воспользоваться ботом {BOT_LINK}.\n"
                   "Скопируй инвайт код ниже, нажми на него, и следуй инструкциям бота.\n"
                   f"{invite_code}")
        return message

    @staticmethod
    async def get_organization_creation_error_message(organization_title, invite_code):
        message = "Ошибка в создании организации"
        return message
