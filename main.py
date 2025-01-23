import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from groq import AsyncGroq

from proxy_config import setup_proxy

setup_proxy()

# Загружаем переменные окружения из файла .env
load_dotenv()

# Инициализация Groq клиента
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

# Установите токен вашего Telegram бота
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Словарь для хранения истории диалогов
user_dialogs = {}

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_dialogs[user_id] = []  # Очищаем историю диалога
    await message.answer("Диалог перезапущен. Задайте ваш вопрос.")

# Обработчик текстовых сообщений
@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    user_message = message.text

    # Добавляем сообщение пользователя в историю диалога
    if user_id not in user_dialogs:
        user_dialogs[user_id] = []
    user_dialogs[user_id].append({"role": "user", "content": user_message})

    # Формируем запрос к Groq API
    chat_completion = await client.chat.completions.create(
        messages=user_dialogs[user_id],
        model="llama3-8b-8192",
    )

    # Получаем ответ от ИИ
    ai_response = chat_completion.choices[0].message.content

    # Добавляем ответ ИИ в историю диалога
    user_dialogs[user_id].append({"role": "assistant", "content": ai_response})

    # Отправляем ответ пользователю
    await message.answer(ai_response)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))