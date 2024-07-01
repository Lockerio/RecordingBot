class UserMessagesTemplate:
    @staticmethod
    async def get_create_profile_message():
        message = ("Введите свое ФИО, пожалуйста. Это нужно, чтобы человек, "
                   "к которому вы записались, понимал кто к нему записался")
        return message

    @staticmethod
    async def get_profile_creation_success_message():
        message = "Профиль успешно создан!"
        return message

    @staticmethod
    async def get_profile_creation_error_message():
        message = "Ошибка в создании профиля"
        return message
