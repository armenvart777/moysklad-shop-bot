import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MOYSKLAD_TOKEN = os.getenv("MOYSKLAD_TOKEN")
MANAGER_USERNAME = os.getenv("MANAGER_USERNAME", "manager")

MOYSKLAD_API_URL = "https://api.moysklad.ru/api/remap/1.2"

# Адреса магазинов (настраиваются под клиента)
STORES = [
    {
        "name": "Магазин 1",
        "address": "г. Город, ул. Примерная, 1",
        "map_url": "https://yandex.ru/maps/...",
    },
    {
        "name": "Магазин 2",
        "address": "г. Город, ул. Примерная, 2",
        "map_url": "https://yandex.ru/maps/...",
    },
]

# Максимум товаров в результатах поиска
MAX_SEARCH_RESULTS = 10

# Максимум символов в запросе
MAX_QUERY_LENGTH = 100
