# Telegram Bot with Groq AI

Этот проект представляет собой Telegram-бота, который использует Groq API для генерации ответов на вопросы
пользователей с помощью модели `llama3-8b-8192`. Бот поддерживает диалог с пользователем, сохраняя контекст разговора.

## Особенности

- **Диалог с ИИ**: Бот отвечает на вопросы пользователя, используя мощь Groq API.
- **Поддержка контекста**: Бот запоминает историю диалога для каждого пользователя.
- **Простота использования**: Бот реагирует только на текстовые сообщения и команду `/start`.

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ваш-username/ваш-репозиторий.git
   cd ваш-репозиторий
    ```
2. **Установите зависимости**:  
   Убедитесь, что у вас установлен Python 3.8 или выше. Затем установите необходимые библиотеки:

    ```bash
    pip install -r requirements.txt
    ```
3. **Создайте файл`.env`**:  
   В корневой директории проекта создайте файл`.env`и добавьте туда ваши API-ключи:

    ```plaintext
    GROQ_API_KEY=ваш_api_ключ_groq
    TELEGRAM_BOT_TOKEN=ваш_токен_telegram_бота
    ```
4. **Настройте прокси (опционально)**:  
   Если вам нужно использовать прокси, укажите их в файле`main.py`:

    ```python
    os.environ['http_proxy'] = 'http://user:password@proxy_ip:port'
    os.environ['https_proxy'] = 'http://user:password@proxy_ip:port'
    ```

## Запуск

Запустите бота с помощью команды:

```bash
python main.py
```

## Использование

1. **Начните диалог**:  
   Отправьте боту команду `/start`, чтобы начать новый диалог.
2. **Задавайте вопросы**:  
   Просто отправьте боту текстовое сообщение, и он ответит вам, используя Groq API.
3. **Перезапуск диалога**:  
   Если вы хотите начать новый диалог, снова отправьте команду `/start`.

## Зависимости

- `aiogram` — для работы с Telegram API.
- `groq` — для взаимодействия с Groq API.
- `python-dotenv` — для загрузки переменных окружения из файла `.env`.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в
файле [LICENSE](https://chat.deepseek.com/a/chat/s/LICENSE).

---

## Автор

[Telegram: Contact @PyAdminRU](https://t.me/PyAdminRU)

