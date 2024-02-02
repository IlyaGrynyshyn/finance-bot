from aiogram import types
from loader import dp, db


@dp.message_handler(commands=["month"])
async def today_statistic(message: types.Message):
    text = db.get_month_statistic(message.from_user.id)
    await message.answer(text)
