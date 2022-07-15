from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (
        "Щоб додати нову витрарту, відправ мені повідомлення в форматані  - сума призначення. \nНаприклад: 500 "
        "продукти\n "
        "Мої команди: \n"
        "1. /today - виводить всі ваші витрати за поточний день\n"
        "2. /month - виводить всі ваші витрати за місяць\n"
        "3. /expenses - виводить останні 10 витрат\n"
        "4. /export - передаю Exel файл з витратами")

    await message.answer(text)
