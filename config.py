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
port = os.getenv("PORT")
ip = os.getenv("IP")
