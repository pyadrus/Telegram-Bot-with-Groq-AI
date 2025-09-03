# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from loguru import logger

# Загружаем переменные окружения из файла .env
load_dotenv()


# Функции для получения переменных окружения
def get_groq_api_key():
    """Возвращает API-ключ для Groq."""
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY не найден в переменных окружения.")
        return api_key
    except Exception as e:
        logger.exception(e)


def get_telegram_bot_token():
    """Возвращает токен Telegram бота."""
    try:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения.")
        return token
    except Exception as e:
        logger.exception(e)


# Настройки прокси
def get_proxy_user():
    """Возвращает логин для прокси."""
    try:
        user = os.getenv("USER")
        if not user:
            raise ValueError("USER (логин прокси) не найден в переменных окружения.")
        return user
    except Exception as e:
        logger.exception(e)


def get_proxy_password():
    """Возвращает пароль для прокси."""
    try:
        password = os.getenv("PASSWORD")
        if not password:
            raise ValueError("PASSWORD (пароль прокси) не найден в переменных окружения.")
        return password
    except Exception as e:
        logger.exception(e)


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
