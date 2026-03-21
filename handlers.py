import html
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import STORES, MANAGER_USERNAME, MAX_SEARCH_RESULTS, MAX_QUERY_LENGTH
from moysklad import search_with_stock

logger = logging.getLogger(__name__)
router = Router()


class UserState(StatesGroup):
    not_verified = State()
    verified = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    # Верификация 18+ при старте
    ...


@router.callback_query(F.data == "age_confirm")
async def age_confirmed(callback: CallbackQuery, state: FSMContext):
    ...


@router.callback_query(F.data == "age_deny")
async def age_denied(callback: CallbackQuery, state: FSMContext):
    ...


async def show_main_menu(message: Message):
    # Главное меню: поиск / адреса / менеджер
    ...


@router.message(UserState.verified, F.text)
async def handle_search(message: Message, state: FSMContext):
    # Поиск по МойСклад с пагинацией
    ...


@router.callback_query(F.data.startswith("more_"))
async def handle_more(callback: CallbackQuery, state: FSMContext):
    # Подгрузка следующей страницы результатов
    ...


@router.message()
async def handle_unverified(message: Message, state: FSMContext):
    ...
