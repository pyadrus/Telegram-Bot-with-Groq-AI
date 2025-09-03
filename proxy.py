# -*- coding: utf-8 -*-
import os

from config import port, ip, user, password


def setup_proxy():
    # Указываем прокси для HTTP и HTTPS
    os.environ['http_proxy'] = f"http://{user}:{password}@{ip}:{port}"
    os.environ['https_proxy'] = f"http://{user}:{password}@{ip}:{port}"


if __name__ == '__main__':
    setup_proxy()
