# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

from config import port, get_proxy_ip, user, password

load_dotenv()  # Загружаем переменные окружения из файла .env

# Установка прокси
proxy_ip = get_proxy_ip()


def setup_proxy():
    # Указываем прокси для HTTP и HTTPS
    os.environ['http_proxy'] = f"http://{user}:{password}@{proxy_ip}:{port}"
    os.environ['https_proxy'] = f"http://{user}:{password}@{proxy_ip}:{port}"


if __name__ == '__main__':
    setup_proxy()
