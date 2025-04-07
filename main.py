import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
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

# Путь к файлу базы знаний
KNOWLEDGE_BASE_PATH = "knowledge_base/data.txt"

# Чтение базы знаний
def load_knowledge_base():
    """Загружает содержимое файла базы знаний."""
    if os.path.exists(KNOWLEDGE_BASE_PATH):
        with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as file:
            return file.read()
    else:
        return "База знаний не найдена. Пожалуйста, создайте файл knowledge_base/data.txt."

# Загружаем базу знаний при запуске
knowledge_base_content = load_knowledge_base()

def remove_markdown_symbols(text: str) -> str:
    """Удаляет символы Markdown (* и **) из текста."""
    return text.replace("*", "")

@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    user_dialogs[user_id] = [
        {"role": "system", "content": f"Ты бот-помощник. Используй эту базу знаний для ответов: {knowledge_base_content}"}
    ]  # Инициализируем диалог с базой знаний
    await message.answer("Диалог перезапущен. Задайте ваш вопрос.")

@dp.message()
async def handle_message(message: Message):
    """Обработчик текстовых сообщений"""
    user_id = message.from_user.id
    user_message = message.text

    # Добавляем сообщение пользователя в историю диалога
    if user_id not in user_dialogs:
        user_dialogs[user_id] = [
            {"role": "system", "content": f"Ты бот-помощник. Используй эту базу знаний для ответов: {knowledge_base_content}"}
        ]
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

    # Отправляем ответ пользователю
    await message.answer(clean_response)

# Ограничение длины истории диалога (опционально)
def limit_dialog_history(dialog, max_length=10):
    """Ограничивает историю диалога до заданного количества сообщений."""
    if len(dialog) > max_length:
        return [dialog[0]] + dialog[-(max_length-1):]  # Сохраняем системное сообщение и последние max_length-1
    return dialog

# Применяем ограничение перед каждым запросом (опционально)
@dp.message()
async def handle_message(message: Message):
    """Обработчик текстовых сообщений с ограничением истории"""
    user_id = message.from_user.id
    user_message = message.text

    if user_id not in user_dialogs:
        user_dialogs[user_id] = [
            {"role": "system", "content": f"Ты бот-помощник. Используй эту базу знаний для ответов: {knowledge_base_content}"}
        ]
    user_dialogs[user_id].append({"role": "user", "content": user_message})

    # Ограничиваем историю диалога
    user_dialogs[user_id] = limit_dialog_history(user_dialogs[user_id])

    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    chat_completion = await client.chat.completions.create(
        messages=user_dialogs[user_id],
        model="llama3-8b-8192",
    )

    ai_response = chat_completion.choices[0].message.content
    user_dialogs[user_id].append({"role": "assistant", "content": ai_response})

    clean_response = remove_markdown_symbols(ai_response)
    await message.answer(clean_response)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))