from aiogram import types
import re
from typing import NamedTuple, Optional

from handlers.errors.error_handler import NotCorrectMassage
from utils.misc.datetime_now import _get_now_formatted

from loader import dp, db
from handlers.errors import error_handler


class Profit(NamedTuple):
    """Структура додавання в БД нового доходу"""

    id: Optional[int]
    owner: int
    amount: int


@dp.message_handler(lambda message: message.text.startswith("+"))
async def add_profit(message: types.Message):
    """
    :param message:
    :return: message.answer
    """
    try:
        profit = add_profit(message.text, message.from_user.id)
    except error_handler.NotCorrectMassage as e:
        await message.answer(str(e))
        return
    answer_message = f"Доданий прибуток в {profit.amount} грн"
    await message.answer(answer_message)


def _parce_message(message: str):
    """
    Парсить текст повідомлення про витрати
    :param message:
    :return: total, category
    """
    parce_result = re.match(r"([\d ]+) (.*)", message)
    print(parce_result)
    if (
        not parce_result
        or not parce_result.group(0)
        or not parce_result.group(1)
        or not parce_result.group(2)
    ):
        raise NotCorrectMassage(
            "Не можу зрозуміти ваше повідомлення. Спробуйте ще раз, використовуючи формат, наприклад:\n "
            "60 кава "
        )

    total = parce_result.group(1)
    return total


def add_profit(raw_message: str, owner):
    """
    Додавання витрати до дази даних
    :param owner:
    :param user_id:
    :param raw_message:
    :return: Expense
    """
    parsed_message = _parce_message(raw_message)
    inserted_row_id = db.add_profit(
        owner=owner,
        amount=parsed_message[1],
        created=_get_now_formatted(),
        raw_test=raw_message,
    )
    return Profit(id=None, owner=owner, amount=parsed_message[1])
