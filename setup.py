# -*- coding: utf-8 -*-
import os

os.system("""pip install -r requirements.txt""")

file = open(".env", "w")
file.write(
    'GROQ_API_KEY=\n'
    'TELEGRAM_BOT_TOKEN=\n'
    'USER=\n'
    'PASSWORD=\n'
    'PORT=\n'
    'IP=\n'
)

# Создание папки для базы знаний
os.mkdir("knowledge_base")

files = open('knowledge_base/data.txt', 'w')
