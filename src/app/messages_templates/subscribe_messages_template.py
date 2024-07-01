class SubscribeMessagesTemplate:
    @staticmethod
    async def get_wait_invite_code_message():
        message = "Введите инвайт код:"
        return message

    @staticmethod
    async def get_subscription_error_message():
        message = "Ошибка подписки на организацию"
        return message

    @staticmethod
    async def get_subscription_success_message(organization_name):
        message = f"Вы подписались на {organization_name}"
        return message
