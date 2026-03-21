import aiohttp
import logging
from config import MOYSKLAD_TOKEN, MOYSKLAD_API_URL

logger = logging.getLogger(__name__)

HEADERS = {
    "Authorization": f"Bearer {MOYSKLAD_TOKEN}",
}


async def search_with_stock(query: str, limit: int = 10, offset: int = 0) -> tuple[list[dict], bool]:
    """Поиск товаров по названию с остатками по каждому складу."""
    async with aiohttp.ClientSession() as session:
        # Поиск товаров через МойСклад API
        products = await _fetch_products(session, query, limit, offset)
        if not products:
            return [], False

        has_more = len(products) > limit
        products = products[:limit]

        # Получаем остатки для каждого товара
        for product in products:
            product["stores"] = await _fetch_stock(session, product["href"])

    return products, has_more


async def _fetch_products(session, query, limit, offset):
    # Запрос к API МойСклад
    ...


async def _fetch_stock(session, product_href):
    # Получение остатков по складам
    ...
