import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ChatAction
from groq import AsyncGroq
from config import get_groq_api_key, get_telegram_bot_token
from proxy_config import setup_proxy

setup_proxy()  # Установка прокси

# Инициализация Groq клиента
client = AsyncGroq(api_key=get_groq_api_key())

# Установите токен вашего Telegram бота
API_TOKEN = get_telegram_bot_token()

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_dialogs = {}  # Словарь для хранения истории диалогов


def remove_markdown_symbols(text: str) -> str:
    """Удаляет символы Markdown (* и **) из текста."""
    return text.replace("*", "")


@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    user_dialogs[user_id] = []  # Очищаем историю диалога
    await message.answer("Диалог перезапущен. Задайте ваш вопрос.")  # Без parse_mode


@dp.message()
async def handle_message(message: Message):
    """Обработчик текстовых сообщений"""
    user_id = message.from_user.id
    user_message = message.text

    # Добавляем сообщение пользователя в историю диалога
    if user_id not in user_dialogs:
        user_dialogs[user_id] = []
    user_dialogs[user_id].append({"role": "user", "content": user_message})

    # Показываем, что бот "печатает"
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    # Формируем запрос к Groq API
    chat_completion = await client.chat.completions.create(
        messages=user_dialogs[user_id],
        model="llama3-8b-8192",
    )

    # Получаем ответ от ИИ
    ai_response = chat_completion.choices[0].message.content

    # Добавляем ответ ИИ в историю диалога
    user_dialogs[user_id].append({"role": "assistant", "content": ai_response})

    # Удаляем символы Markdown (* и **)
    clean_response = remove_markdown_symbols(ai_response)

    # Отправляем ответ пользователю без parse_mode
    await message.answer(clean_response)  # Без parse_mode


# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))