from aiogram import types
from loader import dp, db


@dp.message_handler(commands=["today"])
async def today_statistic(message: types.Message):
    text = db.get_today_statistic(message.from_user.id)
    await message.answer(text)
