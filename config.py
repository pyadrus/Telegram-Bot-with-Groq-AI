# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from loguru import logger

# Загружаем переменные окружения из файла .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")  # Ключ API для Groq
token = os.getenv("TELEGRAM_BOT_TOKEN")  # Токен для Telegram-бота
user = os.getenv("USER")  # Пользователь для прокси
password = os.getenv("PASSWORD")  # Пароль для прокси


def get_proxy_port():
    """Возвращает порт для прокси."""
    try:
        port = os.getenv("PORT")
        if not port:
            raise ValueError("PORT (порт прокси) не найден в переменных окружения.")
        return port
    except Exception as e:
        logger.exception(e)


def get_proxy_ip():
    """Возвращает IP для прокси."""
    try:
        ip = os.getenv("IP")
        if not ip:
            raise ValueError("IP (адрес прокси) не найден в переменных окружения.")
        return ip
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    get_groq_api_key()
    get_telegram_bot_token()
    get_proxy_user()
    get_proxy_password()
    get_proxy_port()
    get_proxy_ip()
