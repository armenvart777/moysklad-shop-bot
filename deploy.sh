#!/bin/bash
# Деплой moysklad_bot на VPS
# Использование: scp -r moysklad_bot/ root@IP:/root/ && ssh root@IP 'bash /root/moysklad_bot/deploy.sh'

set -e

cd /root/moysklad_bot

# Установка Python и venv
apt update && apt install -y python3 python3-venv python3-pip

# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Создание systemd сервиса
cat > /etc/systemd/system/moysklad-bot.service << 'EOF'
[Unit]
Description=MoySklad Telegram Bot
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/moysklad_bot
ExecStart=/root/moysklad_bot/venv/bin/python main.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

# Запуск
systemctl daemon-reload
systemctl enable moysklad-bot
systemctl restart moysklad-bot

echo "Бот запущен! Проверка:"
systemctl status moysklad-bot --no-pager
