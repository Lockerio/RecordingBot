from app.constants.bot_info import BOT_LINK


class OrganizationMessagesTemplate:
    @staticmethod
    async def get_create_organization_message():
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
    async def get_organization_creation_error_message():
        message = "Ошибка в создании организации"
        return message

    @staticmethod
    async def get_active_organization_message(organizations_titles, active_organization_title=None):
        message = ""

        if active_organization_title:
            message += f"Активная организация {active_organization_title}\n\n"
        else:
            message += "Активная организация не выбрана\n\n"

        message += "Список ваших организаций:"
        for organization_title_number, organization_title in enumerate(organizations_titles):
            message += f"\n {organization_title_number + 1}) {organization_title}"

        message += "\n\nДля активации организации, нажмите на соответствующую кнопку"
        return message

    @staticmethod
    async def get_success_organization_setting_message(organization_title):
        message = f"Вы поменяли активную организацию на {organization_title}"
        return message

    @staticmethod
    async def get_error_organization_setting_message():
        message = "Не удалось поменять организацию"
        return message
