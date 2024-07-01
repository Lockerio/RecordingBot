class MainMessagesTemplate:
    @staticmethod
    async def get_start_message():
        message = ("Привет! Я бот для записи на различные мероприятия или занятия. "
                   "Чтобы иметь доступ к моему функционалу необходимо сделать аккаунт (на это уйдет 41 секунда) "
                   "я проверял). Для этого введите команду '/create'.")
        return message
