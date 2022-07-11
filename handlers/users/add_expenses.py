from aiogram import types
import re
from typing import NamedTuple, Optional

from handlers.errors.error_handler import NotCorrectMassage
from handlers.users.categories import Categories
from utils.misc.datetime_now import _get_now_formatted

from loader import dp, db
from handlers.errors import error_handler


@dp.message_handler()
async def add_expense(message: types.Message):
    """
    Додає нову витрату
    :param message:
    :return: message.answer
    """
    try:
        expense = add_expenses(message.text)
    except error_handler.NotCorrectMassage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Додана трана {expense.amount} грн на {expense.category_name}")
    await message.answer(answer_message)


class Expense(NamedTuple):
    """Структура добавленного в БД нового расхода"""
    id: Optional[int]
    amount: int
    category_name: str


def add_expenses(raw_message: str):
    """
    Додавання витрати до дази даних
    :param raw_message:
    :return: Expense
    """
    parsed_message = _parce_message(raw_message)
    categories = parsed_message[1]
    category = Categories().get_categories(categories)
    inserted_row_id = db.add_expense(parsed_message[0], _get_now_formatted(), str(category), raw_message)
    return Expense(id=None, amount=parsed_message[0], category_name=category)


def _parce_message(message: str):
    """
    Парсить текст повідомлення про витрати
    :param message:
    :return: total, category
    """
    parce_result = re.match(r'([\d ]+) (.*)', message)
    if not parce_result or not parce_result.group(0) or not parce_result.group(1) or not parce_result.group(2):
        raise NotCorrectMassage(
            "Не можу зрозуміти ваше повідомлення. Спробуйте ще раз, використовуючи формат, наприклад:\n "
            "50 кава "
        )

    total = parce_result.group(1)
    category = parce_result.group(2)
    return total, category
