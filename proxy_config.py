import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из файла .env

# Логин прокси
USER = os.getenv("USER")
# Пароль прокси
PASSWORD = os.getenv("PASSWORD")
# Порт прокси
PORT = os.getenv("PORT")
# IP прокси
IP = os.getenv("IP")

def setup_proxy():
    # Указываем прокси для HTTP и HTTPS
    os.environ['http_proxy'] = f'http://{USER}:{PASSWORD}@{IP}:{PORT}'
    os.environ['https_proxy'] = f'http://{USER}:{PASSWORD}@{IP}:{PORT}'


if __name__ == '__main__':
    setup_proxy()
