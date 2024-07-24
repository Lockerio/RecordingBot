# RecordingBot (Находится в разработке)

## ТЗ
Необходимо разработать телеграм-бота для записи на различные мероприятия и занятия. 

### Как должно работать
Через организацию можно создать расписание на текущую и наступающую недели. Организацию может создать пользователь с ролью "Основатель" (далее основатель). Данную роль можно получить введя пароль, который выдаст пользователь с ролью "Админ" (далее админ).

Пользователь может подписаться на организацию через ее хэш-код, который направит основатель. Пользователь будет получать уведомления о редактировании расписания и общие сообщения от основателя.

Пользователь может записаться на определенное занятие, основатель получит уведомление об этом.

### Требования

1) В боте должно быть несколько ролей:
    * Админ - администрирование бота;
    * Основатель - ответственный за организацию, расписания и т.д.;
    * Пользователь - пользователь, который может подписываться на организации и записываться на ее мероприятия.
2) Можно создавать расписание на текущую и наступающую неделю;
3) Получение уведомлений от админа (все пользователи), от основателя (подписчики организации).

## Пример работы
Фитнес-тренер создает организацию, рассылает приглашение своим подопечным. Те подписываются на его организацию. 

Тренер создает расписание, всем подписчикам организации придет уведомление. Подопечные записываются на занятия. Тренеру придут уведомления о записи, и у него будет возможность просмотреть список подопечных на определенную тренировку.